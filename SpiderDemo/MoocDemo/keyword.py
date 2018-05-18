import requests
keyword = "python"
kv = {
    "wd" : keyword
}
url = "http://www.baidu.com/s"
try:
    r = requests.get(url,params=kv)
    print(r.raise_for_status())
    print(r.request.url)
    print(len(r.text))
    print(r.text)
except:
    print("失败")