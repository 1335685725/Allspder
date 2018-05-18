import requests
req = requests.get("http://www.santostang.com/")
print("文本编码:",req.encoding)
print("响应状态码:",req.status_code)
content = req.content
print("字节方式的响应体",type(content))  #返回的是bytes类型的内容
print("字符串方式的响应体:",type(req.text)) #返回的是str字符串类型






