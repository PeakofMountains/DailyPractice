# Process.py

from PIL import Image
import numpy as np
import re   # 引入正则表达式
import os

path = r".\trainImages"

#获取训练集和测试集图片名称
def get_img_names(path=path):
    file_names = os.listdir(path)
    img_names = []
    for i in file_names:     # 利用正则表达式，将图片文件名的编号独立出来作为图片的标识
        if re.findall('^\d_\d+\.png$', i) != []:
            img_names.append(i)
    return img_names

# 计算图片像素矩阵，每张图片占一行向量
def get_img_data(img_names):
    pixel_data = []
    for i in img_names:
        img = Image.open(".\\trainImages\\" + i)
        # 训练集和测试集的图片都是黑白图像，因此只取一个颜色通道的像素信息作为特征集即可
        img_vector = np.array(img.split()[0]).reshape(1, 784)[0]
        pixel_data.append(img_vector)
        # 像素数据归一化处理，转换到0-1之间，便于模型训练
    pixel_data = np.array(pixel_data) / 255
    return pixel_data

# 获取图片标签
def get_img_label(img_names):
    n = len(img_names)
    labels = np.zeros([n])  # 根据图片的数量产生零矩阵用来保存标签
    for i in range(len(img_names)):
        labels[i] = img_names[i][0]
        # print(labels[i])
    return labels
# 测试标签的是否成功记录
# names = get_img_names(path)
# get_img_label(names)