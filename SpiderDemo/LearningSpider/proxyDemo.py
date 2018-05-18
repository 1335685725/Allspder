# 使用代理de步骤如下：
# (1) proxy_support = urllib.request.ProxyHandler({})
#     参数是一个字典，字典的键是代理的类型，例如http、ftp或者https，字典的值就是代理的IP地址和对应的端口号
# (2) opener = urllib.request.build_opener(proxy_support)
#     opener可以看作是一个私人订制，当使用urlopen()函数打开一个网页的时候，你就是使用默认的opener在工作
#     而opener是可以定制的，例如，给他定制特殊的headers，或者给他定制指定的代理IP，所以这里使用build_opener（）函数创建一个属于我们私人订制的opener
# (3) urllib.request.install_opener(opener)
#     将定制好的opener安装到系统中，这是一劳永逸的做法，在此之后，你只要使用普通的urlopen()函数，就是以定制好的opener在工作
#     如果你不想替换掉默认的opener，你也可以在每次特殊需要的时候，用opener.open()的方法来打开网页

import urllib.request
url = 'http://www.whatismyip.com.tw/'
# url = "http://www.baidu.com/"
test_proxy = {'https':'183.203.208.166:8118'}
proxy_support = urllib.request.ProxyHandler(test_proxy)
opener = urllib.request.build_opener(proxy_support)
#创建一个包含代理IP的opener
urllib.request.install_opener(opener)
#将代理IP安装进默认环境
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)