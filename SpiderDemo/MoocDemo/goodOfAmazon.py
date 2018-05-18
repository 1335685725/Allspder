import requests
url = "https://www.amazon.cn/dp/0786865660/ref=sr_1_1?ie=UTF8&qid=1518589431&sr=8-1&keywords=book"
kv = {"Cookie":'x-wl-uid=1mKoTtMEXTplBtFanIU3q8/oWZxkw2mtO2xTE/VY1lsGNI08xflPlSzEEarvGkOVj8ML7F8kj/tw=; session-token="pcDkAZyeuBn81h28Otn0QgzbDIZjdnu9tD7QID0c1B85lc4dAXC/PUVnOXzK4u4CWFEe5GdSvbYrbqBWo3yXzv3oCDGOqRSafGkK/6MNshM3bhyMP/bkaSupB/nSZCCXPOigq3v/7aQEpMaJGpC8o1RPM+wWtZB3TQKjczDtwTbPhKnYb4FmawIpeadBwbTUf8wDjw+wxJCpujwpTpf9bbtfWF92v34T6TO9iUVgPtuXbDNUgGoqUQ=="; csm-hit=2X5XXJQKT42CZVHWKJN5+s-AYXEHCQ7QZY0AETBKTH4|1518589913880; ubid-acbcn=457-7344445-1719931; session-id-time=2082729601l; session-id=458-1461202-7214666'
    ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"}
try:
    r = requests.get(url,timeout=10,headers=kv)
    print(r.status_code)
    # r.encoding = r.apparent_encoding
    print(r.headers)
    print(r.text)
except:
    print("faul")
