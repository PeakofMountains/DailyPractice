# 在修改程序内容时不要打开窗口
# 在程序运行之前需要将聊天窗口打开
# 打开的聊天窗口只能是单个窗口
# name可以包含特殊字符，msg内容任意
# 计划之后加入定时发送功能
# 计划之后通过爬虫爬取数据后将数据发送
# 计划之后通过数据库的引用可以将其改造为一个聊天机器人
import win32gui

import win32con

import win32clipboard as w

import time


def send(name, msg):
    # 打开剪贴板

    w.OpenClipboard()

    # 清空剪贴板

    w.EmptyClipboard()

    # 设置剪贴板内容

    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)

    # 获取剪贴板内容

    date = w.GetClipboardData()

    # 关闭剪贴板

    w.CloseClipboard()

    # 获取qq窗口句柄

    handle = win32gui.FindWindow(None, name)

    if handle == 0:
        print('未找到窗口！')

    # 显示窗口

    win32gui.ShowWindow(handle, win32con.SW_SHOW)

    # 把剪切板内容粘贴到qq窗口

    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)

    # 按下后松开回车键，发送消息

    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    time.sleep(1)  # 延缓进程


def main():
    name = 'xxx'  # QQ聊天窗口的名字,
    msg = "xxx"     #要发送的信息
    print('开始')
    send(name ,msg)
    print('结束')


main()
