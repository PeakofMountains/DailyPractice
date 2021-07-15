# ImagePreprocess.py
# 因为从网上找的数据集中的图片大小不一致，不方便之后构建特征集，因此先对所有图片进行大小设置
from PIL import Image   # 调入图片处理类
import os.path
import glob  # 文件操作类
# 将图片的大小统一设置为28*28像素
def convertjpg(jpgfile, outdir, width=28, height=28):
    img=Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
# 对训练集和测试集中的图片进行大小标准化处理
for jpgfile in glob.glob(r".\trainImages\*.png"):
    convertjpg(jpgfile, r".\trainImages")
for jpgfile in glob.glob(r".\testImages\*.png"):
    convertjpg(jpgfile, r".\testImages")