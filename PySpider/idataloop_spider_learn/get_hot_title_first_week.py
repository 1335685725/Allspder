from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    title = []
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read(), "lxml")
        tag_div = soup.find_all("div", {"class": "right-col"})
    except:
        return None
    for tag in tag_div:
        title.append(tag.h2.a["title"])
    return title

title = getTitle("https://www.idataloop.com/ziliao")

for i in title:
    print(i)