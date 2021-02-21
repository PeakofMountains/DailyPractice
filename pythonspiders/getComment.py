import requests # 爬取数据
import re   # 正则匹配
import time # 延时
import pandas as pd # 操纵生成excel




'''
# 需要在网页找到真正的url链接
# 确定浏览器页面需要爬取的内容，进入浏览器调试模式Network，刷新，搜索需爬取内容所在文件位置
# 查看此文件的headers中的Request URL才是真正的url
# 同时记录下此时的cookie和referer以及user-agent
'''
url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=520451341492&spuId=1597412501&sellerId=2271759873&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hv1pvLvZIvUvCkvvvvvjiWPLMy1j3bn2dZtjnEPmPU1jnmPLcUsjrbnLShsjYb9vhvHHif8SJlzHi475%2F1tYAL7rE4gnYpdvhvmpvvwgbkg9CyzUvCvv147SIvwn147DirNYGgvpvhvvvvvUvCvv147AOv%2Bn147Diyqr%2Fevpvhvvmv9F9Cvvpvvvvv29hvCvvvMM%2FgvpvIvvvvvhCvvvvvvUCWphvUIpvv99Cvpv32vvmmvhCvmhWvvUUvphvUpT9Cvv9vvUmq32%2FqeO9CvvOUvvVvJhvUvpCW2V7kvvw5D7zhg8TJEcqhtj7g%2BLp3ZQ0YyX79Re9nfwLWaXp7EcqU1jc6%2Bul1oc7OD70OV161D7zUl8TJPDrrAWBlHdUf8wBlYE7rVpvCvvOvCvvvphmVvpvhvvpvv8QCvvyvCV7mUohvVCZgvpvhvvvvvUvCvv1479%2BvfY147DiiXYGgvpvhvvvvv8QCvCvwC8JCtKOvwE%2Fnrsw6Zf5B&needFold=0&_ksTS=1613913396876_591&callback=jsonp592'
# 伪装成人，浏览器
headers = {
'referer': 'https://detail.tmall.com/item.htm?id=520451341492&ali_refid=a3_430583_1006:1110421683:N:BiD0C5FqmB7ceji94EUHdA==:280791a9d7a93078be1daf2fc8748cbd&ali_trackid=1_280791a9d7a93078be1daf2fc8748cbd&spm=a230r.1.14.1&sku_properties=211948124:8368745',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
'cookie':'lid=%E5%B1%B1%E4%B9%8B%E5%B7%85%E6%B0%B4%E4%B9%8B%E6%B9%84; enc=lFJ0k%2Fyqx5vR%2BhmJAzPB1Pw%2FaN0uk0%2FFdN3nIst4kCHVcXaPe2P4b4XjAt7nw6M0V92tq%2FEfxfWoANo9j8veUj8HIjOhzlXuzd9wdhdu7SI%3D; cna=R3sJFyf8E0kCAXHJiTBIwdDj; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E8tAW3gxC2p4UaMQTZuSs; t=9bd2aa6171659bcf7a4f71bba5ce4c11; tracknick=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; _tb_token_=353ee948eee55; cookie2=1b245d0368b7548f234508fb78dafe86; xlly_s=1; x5sec=7b22726174656d616e616765723b32223a2239643064393139653432663165663762643932383564396635383365333165344350617a79594547454c66366a3748517371766d6951456f416a447475662f632f762f2f2f2f3842227d; isg=BJCQRhAoxCEbGZg4FNuqhmExYd7iWXSjTIfMXophxeuNxTRvMmmiM2DznI0lKyx7; tfstk=cyGlBdMOlYyStjemCQNS71R4XEchZhxz4Xl-gjBDhQRz2DcViCBVQ0bvoooo991..; l=eBERE5JIjS7BG2-ABO5anurza77T0IRfGqVzaNbMiInca6CRNFNs9NCIukb6ldtxgtfjBetPqvMoQRH6JoULRK_ceTwhKXIpBxv9-',
}
# 正则表达式的构建，为了数据清洗
pat = re.compile('"content":"(.*?)"')
datas=[] # 数据列表
for n in range(1, 6):
    # 观察到url中的currentpage后的数字是页数，通过循环改变页数实现爬取多页
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=520451341492&spuId=1597412501&sellerId=2271759873&order=3&currentPage='+str(n)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hv1pvLvZIvUvCkvvvvvjiWPLMy1j3bn2dZtjnEPmPU1jnmPLcUsjrbnLShsjYb9vhvHHif8SJlzHi475%2F1tYAL7rE4gnYpdvhvmpvvwgbkg9CyzUvCvv147SIvwn147DirNYGgvpvhvvvvvUvCvv147AOv%2Bn147Diyqr%2Fevpvhvvmv9F9Cvvpvvvvv29hvCvvvMM%2FgvpvIvvvvvhCvvvvvvUCWphvUIpvv99Cvpv32vvmmvhCvmhWvvUUvphvUpT9Cvv9vvUmq32%2FqeO9CvvOUvvVvJhvUvpCW2V7kvvw5D7zhg8TJEcqhtj7g%2BLp3ZQ0YyX79Re9nfwLWaXp7EcqU1jc6%2Bul1oc7OD70OV161D7zUl8TJPDrrAWBlHdUf8wBlYE7rVpvCvvOvCvvvphmVvpvhvvpvv8QCvvyvCV7mUohvVCZgvpvhvvvvvUvCvv1479%2BvfY147DiiXYGgvpvhvvvvv8QCvCvwC8JCtKOvwE%2Fnrsw6Zf5B&needFold=0&_ksTS=1613913396876_591&callback=jsonp592'
    data = requests.get(url, headers=headers).text
    time.sleep(3)   # 防止爬虫被挡，延时伪装
    datas.extend(pat.findall(data)) # 向数据列表中填充数据


# 创建一个空的数据表
df = pd.DataFrame()
# 数据表列标题
df['追评'] = datas
df.to_excel('C:\\Users\\Administrator\\Desktop\\羽毛球追评.xlsx')    # 指定位置输出excel文件
