import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "
 
 
def getFundList(lst, fundURL):
    html = getHTMLText(fundURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('tr')
    for i in a:
        try:
            id = i.attrs['id']
            lst.append(re.findall(r"[tr]\d{6}", id)[0])
        except:
            continue
 
def getFundInofo(lst, fundURL, fpath):
    count=0
    for fund in lst:
        url = fundURL + fund[1:] + ".html"
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            fundInfo = soup.find('div', attrs={'class': "merchandiseDetail"})
            name = fundInfo.find_all(attrs={'class': "fundDetail-tit"})[0]
            infoDict.update({'基金名称': name.text.split()[0]})
 
            keyList = fundInfo.find_all("dt")
            valueList = fundInfo.find_all("dd")
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
 
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            continue
 
def main():
    fund_list_url = "https://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1"
    fund_info_url = "https://fund.eastmoney.com/"
    output_file = 'D://Fundinfo.txt'
    slist = []
    getFundList(slist, fund_list_url)
    getFundInofo(slist, fund_info_url, output_file)
    print("完成爬取基金信息任务！")
 
main()
