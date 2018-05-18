import requests

url = "https://item.jd.com/4203985.html"
try:
    r = requests.get(url,timeout=10)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
