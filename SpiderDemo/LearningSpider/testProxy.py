import requests

# url = 'http://www.whatismyip.com.tw/'
# url = "http://www.baidu.com/"
url = "https://github.com/"
test_proxy = {'https' : '183.203.208.166:8118'}
headers = {"User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 62.0.3202.94Safari / 537.36"}
req = requests.get(url = url, proxies= test_proxy ,timeout = 10, headers = headers)
req.raise_for_status()
print(req.text)