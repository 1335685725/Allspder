import requests
from bs4 import BeautifulSoup
'''最新需求:获取TOP250电影的中文名字,港台名字,和英文名,以及上映时间,导演,主演,电影分类,以及评分
    并且存储到数据库或者Excel中去,方便查看'''
def getMovie():
    url = "https://movie.douban.com/top250?start="
    headers = {"Host":"movie.douban.com",
               "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 62.0.3202.94Safari / 537.36"}
    movie_list=[]
    for i in range(0,10):
        link = url + str(i * 25)
        req = requests.get(link,headers=headers,timeout=10)
        print( "第"+str(i+1),"页状态响应码:",req.status_code)
        # print(req.text)
        soup = BeautifulSoup(req.text,"lxml")
        div_list = soup.find_all("div",class_="hd")
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list

if __name__ == '__main__':
    movies = getMovie()
    movies=movies.__str__().encode("utf-8")
    with open("TOPMovie.txt","wb") as f:
        f.write( movies)
        f.close()

    print(movies)

