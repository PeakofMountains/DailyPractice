import requests
import os
url = "https://python123.io/ws/demo.html"#爬取页面的网址
root = "D://texts//"#创建文件夹的目录
path = root + url.split('/')[-1]#用url的后面一部分作为文件名
try:
    if not os.path.exists(root):#如果没有相应文件夹，创建文件夹
        os.mkdir(root)
    if not os.path.exists(path):#如果有，写入相应信息
        r=requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
