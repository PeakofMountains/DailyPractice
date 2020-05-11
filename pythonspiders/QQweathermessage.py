import requests
import re
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


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        day = re.findall(r'<h1>(\d+\S+)</h1>', html)
        wea = re.findall(r'<p class=\"wea\" title=\"(\S+)\">', html)
        tem = re.findall(r'<span>(\d+)</span>', html)
        win = re.findall(r'<span class=\"\" title=\"(\S{2,3})\">\S{1,3}级</span>' , html)
        stren = re.findall(r'<span class=\"\" title=\"\S{2,3}\">(\S{1,3}级)</span>', html)
        sun = re.findall(r'<span>(日\S \d{2}:\d{2})</span>',html)

        for i in range(len(day)):
            days = day[i]
            weather = wea[i]
            temperature = tem[i]
            wind = win[i]
            strength = stren[i]
            sunrise = sun[i]
            ilt.append([days, weather, temperature, wind, strength, sunrise])
    except:
        print("")

def main():

    url = "http://www.weather.com.cn/weather1d/101110105.shtml#input"
    html = getHTMLText(url)
    inforList=[]
    parsePage(inforList, html)
    msg = "大家好，现在由我为大家带来天气预报\n" \
          "日期： {:10}\n天气： {:2}\n温度： {:2}℃\n风向： {:3}\n风力：{:2}\n{:10}\n\n日期：{:10}\n天气： {:2}\n温度： {:2}℃\n风向： {:3}\n风力：{:2}\n{:10}\n".format(inforList[0][0]
                    ,inforList[0][1], inforList[0][2],
                    inforList[0][3], inforList[0][4], inforList[0][5],
                    inforList[1][0], inforList[1][1], inforList[1][2],
                    inforList[1][3], inforList[1][4], inforList[1][5])

    name = '妹子立正跟爷走'  # QQ聊天窗口的名字,
    print('开始')
    send(name, msg)
    print('结束')


main()
