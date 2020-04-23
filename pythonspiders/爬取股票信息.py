#CrawBaiduStocksB.py
import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
 
def getStockList(lst, stockURL):
    headers={
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                "cookie": "_m_h5_tk=166731b0915ddca477bd16a43e7e3592_1585816891191; _m_h5_tk_enc=d032c3eb8d5e461387a706a1a2f7f157; thw=cn; cna=R3sJFyf8E0kCAXHJiTBIwdDj; t=abd640f758b630c1e502f27f587c4468; cookie2=7990b8cfe0f228361542e4b4b93df8e0; v=0; _tb_token_=e7eea353de15b; _samesite_flag_=true; sgcookie=E8tAW3gxC2p4UaMQTZuSs; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxdAUzLaiEl3Aoa8%3D&id2=UUphzpYqVZTIEaNfXA%3D%3D&nk2=qlIMvuXNTWFczJJj; csg=f7eb7c68; lgc=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; dnk=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; skt=e8116a80ea30d006; existShop=MTU4NjA3ODQ4Mg%3D%3D; uc4=nk4=0%40qGgm6vyWHbRWZutzHrbxdvx5ZO7VMqY%3D&id4=0%40U2grFbWxcjVo8bJaUrL9Ze%2FOjS2sAbfD; tracknick=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; _cc_=URm48syIZQ%3D%3D; tg=0; enc=lFJ0k%2Fyqx5vR%2BhmJAzPB1Pw%2FaN0uk0%2FFdN3nIst4kCHVcXaPe2P4b4XjAt7nw6M0V92tq%2FEfxfWoANo9j8veUj8HIjOhzlXuzd9wdhdu7SI%3D; tfstk=c98ABewUWYDc7NTlDEnl54kUwOclZlaABS6UWf_I2JtQ6pzOiWLHJHsnc6eAybC..; mt=ci=3_1; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTUPOT6uNLuNg%3D%3D&tag=8&cookie21=W5iHLLyFe3xm&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&lng=zh_CN&existShop=false&pas=0; JSESSIONID=9FAD1A8DE4C77E3BAF85502D89550F8C; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; isg=BPz8D1cVjgYRELraJI0x62EbzZqu9aAfdBu609Z8jefKoZ0r_wTerxhTgcnZ6dh3; l=dBTJ6e-PQXUZPR7LBOfNlFSosP7tiIdb8sPyQ4mUaICPO31657_GWZf__YLBCnGVHsIyJ3oGfmN0B-TF9yCqJxpsw3k_J_DmndC.."
            }
    html=requests.get(stockURL,headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
 
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
 
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
             
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
             
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            continue
 
def main():
    stock_list_url = "https://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "D:/BaiduStockInfo.txt"
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()
