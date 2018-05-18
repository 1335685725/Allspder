from io import BytesIO
import pytesseract
import requests
import tablib
from PIL import Image
from bs4 import BeautifulSoup




class Spider(object):
    def __init__(self, account, pwd):
        self.getCaptchaUrl = 'http://my.ujs.edu.cn/captchaGenerate.portal'
        self.loginUrl = 'http://my.ujs.edu.cn/userPasswordValidate.portal'
        self.getScoreUrl = 'http://my.ujs.edu.cn/index.portal?.pn=p2365_p2536'
        self.session = requests.Session()
        self.loginSuccess = False
        self.account = account
        self.pwd = pwd
        self.login_time = 0

    def login(self):
        self.login_time +=1
        print(self.login_time)
        r = self.session.get(self.getCaptchaUrl)
        image = Image.open(BytesIO(r.content))
        code = pytesseract.image_to_string(image)

        data = {
            'Login.Token1': self.account,
            'Login.Token2': self.pwd,
            'captchaField': code.encode('utf-8'),
            'goto': 'http://my.ujs.edu.cn/loginSuccess.portal',
            'gotoOnFail': 'http://my.ujs.edu.cn/loginFailure.portal'
        }
        r1 = self.session.post(self.loginUrl, data)
        self.loginSuccess = 'handleLoginSuccessed' in r1.text

    def get_score(self):
        r = self.session.get(self.getScoreUrl)
        soup = BeautifulSoup(r.text, "html.parser")
        tr_list = soup.select('.portlet-table tr')
        headers = [x.text for x in tr_list[0].select('th')]
        data = tablib.Dataset()
        data.headers = headers
        for i in tr_list[1:]:
            data.append([x.text for x in i.select('td')])
        with open('./历年成绩.xls', 'wb') as f:
            f.write(data.export('xls'))
            print("\n成绩导出成功")

    def main(self):
        while not self.loginSuccess:
            self.login()
        self.get_score()


if __name__ == '__main__':
    spider = Spider(3160212052, '1335685725')
    spider.main()
