import urllib.request as request
from bs4 import BeautifulSoup
import re

html = request.urlopen("http://www.pythonscrapping.com/pages/page3.html")
soup = BeautifulSoup(html,"html.parser")

imagens = soup("img",{'src':re.compile(r"\.{2}/img/gifts/img\d*\.jpg")})

for imagem in imagens:
    print (imagem['src'])