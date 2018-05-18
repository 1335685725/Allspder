import requests
from lxml import etree
import copy
import json


url = "https://www.imooc.com/course/list?c=python&page="
headers = {"User-Agent": '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'''
           }
all_course = []
course_dict = {}

def main(url, headers):
    for i in range(1, 3):
        a_url = url + str(i)
        print(f"开始爬取第{i}页\n{a_url}")
        html = requests.get(url=a_url, headers=headers)
        content = etree.HTML(html.text)

        titles = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/div[2]/h3/text()")
        urls = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/@href")
        levels = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/div[2]/div[1]/div[1]/span[1]/text()")
        studied_people = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/div[2]/div[1]/div[1]/span[2]/text()")
        descriptions = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/div[2]/div[1]/p/text()")

        for i in range(len(titles)):
            course_dict["title"] = titles[i]
            course_dict["urls"] = "https://www.imooc.com" + urls[i]
            course_dict["levels"] = levels[i]
            course_dict["studied_people"] = studied_people[i]
            course_dict["descriptions"] = descriptions[i]
            copied_dict = copy.deepcopy(course_dict)
            all_course.append(copied_dict)
        print("--------------------------------------------------")
        # print(len(all_course))
    # 写到json文件中
    with open("慕课网python教程.json", "w") as f:
        json.dump(all_course, f, ensure_ascii=False, sort_keys=True, indent=4)
        print("success")


main(url, headers)






