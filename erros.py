import urllib.request as request
from urllib.request import HTTPError, URLError
from bs4 import BeautifulSoup

html = request.urlopen("http://localhost:8000")
print(f"HTML_1: {html}")
bsObj = BeautifulSoup(html.read(),"html.parser")
try:
    resultado = bsObj.tag_nao_existente
    print(resultado)
except AttributeError as erro:
    print("ATT eRROR")

try:
    html = request.urlopen("http://localhost:8000/teste.html")
    print(f"HTML_2: {html}")
except HTTPError as erro:
    print(f"ERRO: {erro}")

try:
    html = request.urlopen("http://gosto.de.batata")
    print(f"HTML_3: {html}")
except URLError as erro:
    print(f"ERRO: {erro}")
