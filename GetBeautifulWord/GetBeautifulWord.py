import requests
import os
import time


url = "https://chp.shadiao.app/api.php"             # Postman自动生成的访问请求代码

payload = {}
headers = {
  'authority': 'chp.shadiao.app',
  'accept': '*/*',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://chp.shadiao.app/?from_nmsl',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': '__gads=ID=4b672a2f78b27cf7:T=1587813875:S=ALNI_Ma0_TT8Rz29zyD5zjrkEyeNmDbKdg; Hm_lvt_0237bad9496c62f26747ca19a52eca1a=1587813872,1589700963,1589728979,1590231630; Hm_lpvt_0237bad9496c62f26747ca19a52eca1a=1590231840'
}
dirpath = "F:/BeautifulWords/"                  # 创建文件夹的目录
filepath = dirpath + "BeautifulWords.txt"       # 用指定文件路径
def main():
    response = requests.request("GET", url, headers=headers, data = payload)
    time.sleep(10)              # 每10秒执行一次，防止给网站服务器太大压力
    # print(response.text)      # 展示返回html的内容，这个网站比较特殊，返回的就刚好是我想要的文本
    try:
        if not os.path.exists(dirpath):            # 如果没有相应文件夹，创建文件夹
            os.mkdir(dirpath)
        with open(filepath, 'a') as f:              # 这里采用'a'追加写模式
            f.write(response.text+"\n")
            f.close()
            print("文件保存成功")
    except:
        print("爬取失败")


while True:
    main()