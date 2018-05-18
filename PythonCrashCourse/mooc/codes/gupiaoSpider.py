import requests
import re
from bs4 import BeautifulSoup
import traceback


def getHTML(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding  需要进行分析，很浪费时间的，
        r.encoding = code
        return r.text
    except:
        print("失败了")
        return ''

def getStockList(List, stockURL):
    html = getHTML(stockURL, 'GB2312')
    soup = BeautifulSoup(html,"lxml")
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.a['href']
            List.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fPath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTML(url)
        try:
            if html == "":
                continue
            infoDic = {}
            soup = BeautifulSoup(html,"lxml")
            stockInfo = soup.find("div",attrs={'class': 'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDic.update({"股票名称":name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDic[key] = val
            with open(fPath,'a',encoding="utf-8") as f:
                f.write(str(stockInfo) + "\n")
                count = count + 1
                print('\r当前速度：{:.2f}%'.format(count*1000/len(lst)),end="")
        except:
            count = count + 1
            print('\r当前速度：{:.2f}%'.format(count * 1000 / len(lst)), end="")
            traceback.print_exc()
            continue


def main():
    stock_list_url = "https://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    ouput_file = "BaiduGupiao.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, ouput_file)

main()



