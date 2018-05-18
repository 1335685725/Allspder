
import requests
from lxml import etree

html = requests.get("https://www.imooc.com/course/list?c=python&page=2").text

content = etree.HTML(html)

title = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/div[2]/h3/text()")
"//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div"
"//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/@href"
urls = content.xpath("//*[@id=\"main\"]/div[2]/div[2]/div[1]/div//div/a/@href")
print(title)
print(urls)


