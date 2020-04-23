import requests
import re
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(":")[1])
            title=eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print("")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
    print("")
def main():
    goods="耳机"
    depth=1
    start_url="https://s.taobao.com/search?q="+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url +"&s="+str(44*i)
            headers={
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                "cookie": "_m_h5_tk=166731b0915ddca477bd16a43e7e3592_1585816891191; _m_h5_tk_enc=d032c3eb8d5e461387a706a1a2f7f157; thw=cn; cna=R3sJFyf8E0kCAXHJiTBIwdDj; t=abd640f758b630c1e502f27f587c4468; cookie2=7990b8cfe0f228361542e4b4b93df8e0; v=0; _tb_token_=e7eea353de15b; _samesite_flag_=true; sgcookie=E8tAW3gxC2p4UaMQTZuSs; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxdAUzLaiEl3Aoa8%3D&id2=UUphzpYqVZTIEaNfXA%3D%3D&nk2=qlIMvuXNTWFczJJj; csg=f7eb7c68; lgc=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; dnk=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; skt=e8116a80ea30d006; existShop=MTU4NjA3ODQ4Mg%3D%3D; uc4=nk4=0%40qGgm6vyWHbRWZutzHrbxdvx5ZO7VMqY%3D&id4=0%40U2grFbWxcjVo8bJaUrL9Ze%2FOjS2sAbfD; tracknick=%5Cu5C71%5Cu4E4B%5Cu5DC5%5Cu6C34%5Cu4E4B%5Cu6E44; _cc_=URm48syIZQ%3D%3D; tg=0; enc=lFJ0k%2Fyqx5vR%2BhmJAzPB1Pw%2FaN0uk0%2FFdN3nIst4kCHVcXaPe2P4b4XjAt7nw6M0V92tq%2FEfxfWoANo9j8veUj8HIjOhzlXuzd9wdhdu7SI%3D; tfstk=c98ABewUWYDc7NTlDEnl54kUwOclZlaABS6UWf_I2JtQ6pzOiWLHJHsnc6eAybC..; mt=ci=3_1; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTUPOT6uNLuNg%3D%3D&tag=8&cookie21=W5iHLLyFe3xm&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&lng=zh_CN&existShop=false&pas=0; JSESSIONID=9FAD1A8DE4C77E3BAF85502D89550F8C; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; isg=BPz8D1cVjgYRELraJI0x62EbzZqu9aAfdBu609Z8jefKoZ0r_wTerxhTgcnZ6dh3; l=dBTJ6e-PQXUZPR7LBOfNlFSosP7tiIdb8sPyQ4mUaICPO31657_GWZf__YLBCnGVHsIyJ3oGfmN0B-TF9yCqJxpsw3k_J_DmndC.."
            }
            html=requests.get(url,headers=headers)
            parsePage(infoList,html.text)
        except:
            continue
    printGoodsList(infoList)
    
main()
