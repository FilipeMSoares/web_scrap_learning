import urllib.request as request
from urllib.request import Request
from bs4 import BeautifulSoup

html = request.urlopen("http://evaldowolkers.wordpress.com")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.h1)
print(bsObj.find_all('a'))
for link in bsObj.find_all('a'):
    print(link.get('href'))

teste = bsObj.findAll("",{"class":"comments-link"})
for a in teste:
    print(a)

teste = bsObj.findAll(text="Python")
for a in teste:
    print(a)

print(bsObj.get_text())
print(bsObj.title)
print(bsObj.title.name)
print(bsObj.title.string)
print(bsObj.title.parent)
print(bsObj.title.parent.name)
print(bsObj.body['class'])
print(bsObj.find(id="menu-item-147"))