'''##############################################################################
* @File name: PlayPianogame.py
* @Author: PeakofMountains
* @Version: 1.1
* @Date: 2020-5-19
* @Description: Auto play piano game. 本程序以4399中的别再踩白块了游戏作为例子
##############################################################################'''
import pyautogui    # 实现自动点击
import time         # 实现延时


pyautogui.FAILSAFE = True   # 防止鼠标被程序一直占用无法终止程序，这里实现鼠标移到屏幕的四个角程序就异常终止
time.sleep(5)               # 由程序切换到游戏界面的时间


def main():
    image = (490, 720, 480, 10)     # 根据自己屏幕的大小，用截图的方式获得图片的左上角坐标及截图的长、高
    im = pyautogui.screenshot(region=image)     # 对指定位置指定大小进行截图
    # im.save('test.jpg')   # 这里可以将截图保存到当前目录查看截图位置是否正确
    # x = 60, y = 5         # 起始位置
    x = 60
    for i in range(4):      # 判断四个位置
        px = im.getpixel((x,5)) # 这里的getpixel()只接受一个参数，传入坐标即可(括号括起来)，获得RGB值
        # 得到的px是保存RGB坐标的元组
        if (px[0] == 1):    # 判断是否为黑色,是黑色就点击， 黑色的RGB是（1,1,1）
            pyautogui.click(image[0] + x, image[1] + 5)   # 注意此处点击的是整个屏幕的位置
        x += 120            # 下一个点


while True:                 # 一直执行
    main()


