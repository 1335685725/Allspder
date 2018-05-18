import requests
'''
key_dict = {"key1":"value1","key2":"value2"}
r = requests.get("http://www.santostang.com",params=key_dict)
print("URL已经正确编码",r.url)
print("字符串响应体:",r.text)
'''
# 发送get请求
headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Host":"www.santostang.com"}
r1 = requests.get(url="http://www.santostang.com/", headers=headers)
print("状态响应码:",r1.status_code)

key_dict = {"key1":"value1","key2":"value2"}
r2 = requests.post("http://www.santostang.com",params=key_dict, timeout=100)
print(r2.text)

