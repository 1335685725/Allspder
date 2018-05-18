# -*- coding:utf-8 -*-
#爬元尊第一章
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    target = "http://www.biqudu.com/31_31729/2170175.html"
    req = requests.get(url=target)
    req.encoding = "utf-8"
    html = req.text
    bf = BeautifulSoup(html,'html.parser')
    texts = bf.find_all("div",id="content")
    realText = texts[0].text.replace("\xa0"*8,"\n\n")
    print(realText)
# with open("first.txt","wb") as f:
#     f.write(bytes(realText.encode("utf-8")))