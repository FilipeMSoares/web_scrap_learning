import urllib.request as request
from bs4 import BeautifulSoup
import re

url = r"http://www.folha.uol.com.br"
req = request.Request(url=url,headers={'User-Agent':'Mozilla-5.0'})
html = request.urlopen(req)

soup = BeautifulSoup(html.read(),"html.parser")

print(soup.title)
print(soup.a['href'])

regex = r"(.)*folha\.uol\.com\.br/poder/2019/08(.)*\.shtml"

links = soup.findAll(name="a",attrs={"href":re.compile(regex)})

for link in links:
    print(link['href'])
