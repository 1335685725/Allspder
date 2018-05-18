import requests

'''A Test spiding baidu index'''
def getUrl(url):
    try:
        r = requests.get(url, timeout=10)
        r.status_code
        r.encoding = r.apparent_encoding
    except:
        print("a except raise")
    return  r.text
    #text 返回的是str形式，也就是字符形式
    #content返回的是二进制形式
'''
    str转换成content 也就是字符转换成二进制的过程称为编码，用的是encod
    二进制转换成字符形式的过程称为解码，用的是decodee
'''
if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(type(getUrl(url)))
    print(getUrl(url))

