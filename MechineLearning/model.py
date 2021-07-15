# model.py
import tensorflow as tf
import PrepareModel
# 在tensorflow2.0版本之后去除了placeholder()函数，因此这里我调用1.0版本的tensorflow使用
tf = tf.compat.v1
tf.disable_v2_behavior()

# 模型如下
# 先定义会话
sess = tf.compat.v1.InteractiveSession()
# 设置占位符
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

# 定义权重
def weight_variable(shape):
  initial = tf.random.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
# 定义偏置量
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)
# 定义卷积函数
def conv2d(x, w):
  return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')
#定义池化函数
def max_pool_2x2(x):
  return tf.nn.max_pool2d(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# 定义第一层卷积核filter和偏置量，偏置量的维度是32
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# 将输入tensor进行形状调整，调整成为一个28*28的图片，与规格化处理后的训练图片保持一致
x_image = tf.reshape(x, [-1,28,28,1])

# 进行第一层卷积操作，得到线性变化的结果，再利用relu规则进行非线性映射，得到第一层卷积结果h_conv1。
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

# 采用了最大池化方法，最终得出池化结果h_pool1
h_pool1 = max_pool_2x2(h_conv1)

# 定义第二层卷积核filter和偏置量，偏置量的维度是64.
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

# 第二层卷积和池化结果
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 定义全连接层的权重和偏置量
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

# 将第二层池化后的数据调整为7×7×64的向量
# 再与全连接层的权重进行矩阵相乘，然后进行非线性映射得到1024维的向量。
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.compat.v1.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层的权重和偏置量
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

# 添加softmax，得到输出结果
y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 计算损失函数
cross_entropy = -tf.reduce_sum(y_*tf.math.log(y_conv))
# 采用梯度下降法
train_step = tf.compat.v1.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# 模型精度
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# 模型训练如下

# 通过tf执行全局变量的初始化，然后启用session运行图。
sess.run(tf.compat.v1.global_variables_initializer())
# 总共经过500次迭代，每次迭代给模型随机喂送20个训练样本
for i in range(500):
  batch = PrepareModel.next_batch(20)
  batch_feature = batch[0]
  batch_label = batch[1]
  if i % 100 == 0:
    train_accuracy = accuracy.eval(feed_dict={x: batch_feature, y_: batch_label, keep_prob: 1.0})
    print("经过 %d 轮迭代------------------ ----->实现手写数字识别训练集精度达到 %.2f" % (i, train_accuracy))
  train_step.run(feed_dict={x: batch_feature, y_: batch_label, keep_prob: 0.5})
# 测试最终的识别效果,keep_prob=1表示所有元素全部被保留
print("-------------------最终手写数字识别测试集精度 %.2f---------------------" % accuracy.eval(feed_dict={x: PrepareModel.test_feature, y_: PrepareModel.test_labels, keep_prob: 1.0}))
# 从结果来看，经过400次迭代后，训练集的精度就已经达到了1.00，出现这种情况我认为有以下原因：
# 1. 使用的卷积神经网络模型能很大限度地保留图片的二维信息
# 2. 训练集和测试集的样本数据不多
# 3. 测试用的图片与训练用的图片相似度较高

