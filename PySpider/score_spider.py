import requests
from bs4 import BeautifulSoup
import xlwt
import getpass
import os
# 创建excel文件
try:
    file = xlwt.Workbook()
except Exception as e:
    print(e)
table = file.add_sheet("score", cell_overwrite_ok=True)
id = input("enter your id:")
password = input("enter your password:")
# password = getpass.getpass("enter your password:")


# 成绩页面的url
url = "http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536"
header = {"Host": "my.ujs.edu.cn",
"Referer": "http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

yzm=""
with requests.Session() as s:

    print("\n请稍等，正在爬取数据...\n")
    # req1 = s.get(url=url, )
    req1 = s.get(url)
    url2 = req1.url
    req1.encoding = "urf-8"
    html = req1.text
    soup0 = BeautifulSoup(html, "lxml")
    soup0.find_all()


    data = {"user": id, "pwd": password, "captcha": yzm}







    # tr_score = soup0.find_all("tr", {"class": "portlet-table-odd"})
    # head = []
    # for i in tr_score[0].th:
    #     head.append(i.text)
    # for i in range(len(head)):
    #     table.write(0, i, head[i])
    #
    # scores = []
    # for a in range(len(tr_score)-1):
    #     a +=1
    #     for th_list in tr_score[1:]:
    #         i = 0
    #         for th_data in th_list.th:
    #             table.write(a, i, th_data.text)
    #             i +=1
    #
    # table.save("score.xls")

