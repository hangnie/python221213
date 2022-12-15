# web2.py

#서버와 통신
import urllib.request
#웹크릴링
from bs4 import BeautifulSoup

#파일에 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

#페이징을 처리(각 페이지에 10개의 데이터)
for i in range(1,6):

    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    data = urllib.request.urlopen(url)
    print(url)
    #검색이 용이한 객체
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    for tag in cartoons:
        title = tag.find("a").text
        print(title.strip())
        f.write(title.strip() + "\n")

f.close()

