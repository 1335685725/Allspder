import requests
from bs4 import BeautifulSoup

url = "http://www.santostang.com/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
r = requests.get(url,headers=header)
# print(r.text)
soup = BeautifulSoup(r.text,"lxml")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)
with open("title.txt","ab+") as f:
    f.write(bytes(title.encode("utf-8")))
    f.close()
