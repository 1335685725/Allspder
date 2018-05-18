import requests
from bs4 import BeautifulSoup
ip = input("请输入要查询的IP:")
#测试IP：202.204.80.112
# BeautifulSoup.prettify()用于更好的输出HTML格式 Ex: print(Soup.prettify())
kv = {
    "ip":ip
}
url = "http://www.ip138.com/ips138.asp"
try:
    r = requests.get(url,params=kv,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("faul")
bs = BeautifulSoup(r.text,"html.parser")
#lxml也可以替代html.parser
'''
    解析器类型： html.parser 属于bs4库
                lxml属于lxml库 
                xml属于lxml库
                html5lib属于html5lib库  都可以通过pip安装
'''
res = bs.find("ul",class_="ul1")#<class 'bs4.element.Tag'>
# print(type(res))
# print(res.contents)
# for tag in res.contents:
#     print(tag.string)
for tag in res.children:
    print(tag.string)

#遍历后续节点
# for sibling in soup.a.next_siblings:
#     print(sibling)
#遍历前序节点
# for sibling in soup.a.previous_siblings:
#     print(sibling)


