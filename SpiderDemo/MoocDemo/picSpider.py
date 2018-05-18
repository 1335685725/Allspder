import requests
import os
root = "D://pic//"
url = "http://image.nationalgeographic.com.cn/2018/0130/20180130113825933.jpg"
#将图片的名字分离开来
path = root + url.split("/")[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)#创建文件夹
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path ,'wb') as f:
            f.write(r.content)
            f.close()
            print("保存成功")
    else:
        print("文件已存在")
except:
        print("faul")