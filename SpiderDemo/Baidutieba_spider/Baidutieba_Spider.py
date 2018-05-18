import requests




#定义一个函数，用于爬取对应的数据
def load_url(url,file_name,kv):
    '''
    作用：针对指定的url进行数据的爬取
    :param url:要爬取的地址
    :param file_name:要保存的文件名称；在当前函数中，制作提示作用
    :return:爬取的数据
    '''

    print("开始爬取%s的数据"%file_name)
    #爬取程序
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    req = requests.get(url,headers=headers,params=kv)
    req.encoding = req.apparent_encoding
    print('爬取%s的内容完成！' % file_name)
    return req.text
#定义一个函数，用于保存数据
def save_data(data,file_name):
    '''
    作用：保存爬取下来的数据
    :param data: 爬取的数据
    :param file_name: 要保存的文件名字
    :return: 无
    '''
    print("开始保存%s的内容"%file_name)
    with open(file_name,"w",encoding='utf-8') as f:
        #在windows下面，新文件的默认编码是gbk
        f.write(data)
    print("保存%s的内容成功"%file_name)

#定义一个函数，进行爬虫的核心处理功能
def spider(url,name,begin,end):
    '''
    用于进行核心爬虫功能的调度
    :param url:要爬取的网址
    :param name:贴吧名称
    :param begin:开始爬取的页码
    :param end:结束页码
    :return:无
    '''
    for page in range(begin,end+1):
        #计算需要的页码
        global pn
        pn = (page-1)*50
        #进行tieba_name的参数设置
        kv = {
            "ie": "utf-8", "kw": name, "pn": pn
        }
        # 拼接url地址
        #定义一个保存文件的名臣
        file_name = "网页"+ str(page)+".html"
        #开始爬取数据
        html = load_url(url,file_name,kv)
        #保存数据到文件
        save_data(html,file_name)

if __name__ == '__main__':
    #用户输入相关数据
    try:
        url = "http://tieba.baidu.com/f?"
        name = input("请输入要爬取的贴吧的名称:")
        begin = int(input("请输入要爬取的开始页码："))
        end = int(input("请输入要爬取的结束页码："))
    except:
        print("请正确输入参数")

    #执行爬虫
    spider(url,name,begin,end)














