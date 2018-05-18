import re
import requests


'''淘宝搜索比价爬虫'''

def getHTML(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '失败'

def parsePage(info_List,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            info_List.append([price,title])
    except:
        print("")

def printGoodList(info_List):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in info_List:
        count +=1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '书包'
    deepth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    info_List = []
    for i in range(deepth):
        try:
            url = start_url + '&s=' + str(i*44)
            html = getHTML(url)
            parsePage(info_List,html)
        except:
            continue
    printGoodList(info_List)

main()



