# wep2.py

#서버와 통신
import urllib.request
#웹크릴링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
print("길이:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title.strip())
print(link.strip())

for tag in cartoons:
    title = tag.text.strip()
    print(title)

