# PrepareModel.py

# 随机取batch_size个训练样本
import numpy as np
import pandas as pd
from Process import *   # 调用Process文件中的多个处理函数后的特征集和标签集

# 获得训练集的特征集
train_img_names = get_img_names()
train_feature = get_img_data(train_img_names)

# 将编号用数字表示，则数据不能直接用在模型中，因为模型往往默认数据数据是连续有序的。
# 但是，按照我们上述的表示，数字并不是有序的，而是随机分配的，因此通过使用独热编码的方法解决此问题。
# 获得训练集的标签集，转为独热编码
train_labels = get_img_label(train_img_names)
train_labels = np.array(pd.get_dummies(np.array(train_labels)))

# 测试集的特征集
test_path = r".\testImages"
test_img_names = get_img_names(path=test_path)
test_feature = get_img_data(test_img_names)
# 测试集的标签集，也转为独热编码
test_labels = get_img_label(test_img_names)
test_labels = np.array(pd.get_dummies(np.array(test_labels)))

# batch_size
def next_batch(batch_size,train_data = train_feature, train_target = train_labels):
    # 打乱数据集的顺序
    index = [i for i in range(0, len(train_target))]
    np.random.shuffle(index);
    # 建立batch_data与batch_target的空列表
    batch_data = []
    batch_target = []
    # 向空列表加入训练集及标签
    for i in range(0, batch_size):
        batch_data.append(train_data[index[i]])
        batch_target.append(train_target[index[i]])
    batch_data = np.array(batch_data)
    batch_target = np.array(batch_target)
    # 返回这两个列表
    return batch_data, batch_target
