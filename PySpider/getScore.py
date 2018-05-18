import requests
from bs4 import BeautifulSoup
import xlwt




data = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=0001W6BWEHVFxRBV4LsJCyu1U8V:1G29UH6J81; iPlanetDirectoryPro=AQIC5wM2LY4SfczIrBZT9gSjGHzih3JXk82uJu70jdke0CA%3D%40AAJTSQACMDE%3D%23",
        "Host": "my.ujs.edu.cn",
        "Referer": "http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
try:
    file = xlwt.Workbook()
except Exception as e:
    print(e)
table = file.add_sheet("score", cell_overwrite_ok=True)
req = requests.get("http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536", headers=data)
req.encoding = "utf-8"
html = req.text
# print(html)
print("爬取成功")
soup0 = BeautifulSoup(html, "lxml")

th_head = soup0.find("tr", {"class": "portlet-table-odd"}).find_all("th")
head = [i.string for i in th_head]
for i in range(len(head)):
    table.write(0, i, head[i])

tr_scores1 = soup0.find_all("tr", {"class": "portlet-table-odd portlet-table-down"})
# print(tr_scores1)
tr_scores2 = soup0.find_all("tr", {"class": "portlet-table-even"})
# print(tr_scores2)
tr_scores1.extend(tr_scores2)
tr_scores = tr_scores1
i = 1
for tr_score in tr_scores:
    j = 0
    for td in tr_score.find_all("td"):
        table.write(i,j,td.string)
        j+=1
    i+=1


file.save("score1.xls")
print("文件保存成功")

