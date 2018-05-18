import requests
from PIL import Image
from bs4 import BeautifulSoup
import os
import xlwt
import re

def get_captcha(si_code):
    captcha_url = "http://my.ujs.edu.cn/" + si_code
    print(captcha_url)
    r = session.get(captcha_url, headers=header)
    with open("captcha.jpg","wb") as f:
        f.write(r.content)
    try:
        im = Image.open("captcha.jpg")
        im.show()
        im.close()
    except:
        print(f"请到 {os.path.abspath('captcha.jpg')} 目录下 找到captcha.jpg文件手动输入")
    captcha = input("please input the captcha\n")
    return captcha


def get_si_code(url):
    # si_code是一个动态变化的参数
    index_page = session.get(url, headers=header)
    html = index_page.text
    # print(html)
    soup = BeautifulSoup(html, "lxml")
    si_code = soup.find("img", {"id":"captchaImg"})["src"]
    # for i in si_code:
    #     print(i)
    print(si_code)
    return si_code

def login(user, pwd, si_code, url):
    post_data = {
        "username": user,
        "pwd": pwd,
        "captcha": si_code,
    }
    post_data["captcha"] = get_captcha(si_code)
    # 登陆
    login_page = session.post(url, data=post_data, headers=header)
    print(login_page.status_code)



if __name__ == '__main__':
    url = "http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536"
    header = {"Host": "my.ujs.edu.cn",
              "Referer": "http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536",
              "Upgrade-Insecure-Requests": "1",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

    session = requests.session()
    session.get(url, headers=header)
    # 获取验证码
    si_code = get_si_code(url)
    id = input("enter your id:")
    password = input("enter your password:")
    login(id, password, si_code, url)





