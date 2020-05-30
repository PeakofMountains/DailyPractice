'''
# @Author: PeakofMountains
# @FileName: ToCharPicture.py
# @Date: 2020-05-30
# @Version: 1.1
# Description: Using characters to show a picture
# Problem: 目前只有简单的图像转换之后能看清，复杂的图像转换后分辨率不高
'''
from PIL import Image   # 图像处理库
import sys              # 获取命令行参数用的


def resize_image(image):    # 改变图片的尺寸
    w, h = image.size       # 指定宽、高
    target_w = 100          # 设置希望显示的宽度，不知道为什么我这里只有当宽度设定为100时效果最好
    aspect_ratio = h/float(w)   # 计算高宽比
    target_h = int(target_w * aspect_ratio*0.66)    # 根据高宽比确定高度，能保证图片的比例不变，也可以想这里的*0.66一样自己改变比例
    new_image = image.resize((target_w, target_h))  # 确定显示的宽高
    return new_image


# 从命令行获取图片文件路径
if __name__=='__main__':
    image_path = "D:\Demo.png"      # 在程序中直接指定图片路径
    # image_path = sys.argv[1]        # 实现通过命令行的执行参数确定图片所在路径
    image = Image.open(image_path)      # 得到图片文件
    new_image = resize_image(image)        # 改变图片大小

# 图片转灰度
def convert_image(image):
    gray_image = image.convert('L')
    return gray_image


def get_img_pixel(image):
    pixels = image.getdata()    # 获取图片像素的灰度值
    return pixels


# 替换为字符
def change_pixles_to_chars(pixels):
    new_pixels = []
    for pixel_value in pixels:
        n = 25
        index = pixel_value//n         # 225除以填充字符种类数应该等于这里的n
        new_pixels.append(chars[index])

    return ''.join(new_pixels)


# 这里是填充字符的列表，数量由自己选择
chars = ['a', 'l', 'o', 'v', 'e', 'l', 'y', 'g', 'i', 'r', 'l']
gray_image = convert_image(new_image)
pixels = get_img_pixel(gray_image)
new_pixels = change_pixles_to_chars(pixels)
len_pixels = len(new_pixels)
char_image = [new_pixels[index:index+100]for index in range(0, len_pixels, 100)]
print('\n'.join(char_image))
# for i in pixels:  # 测试输出像素的RGB值
#     print(i, end=',')