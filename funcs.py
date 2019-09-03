import urllib.request as request
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup

def get_all_h1(url):
    try:
        html = request.urlopen(url)
    except HTTPError as erro:
        print(f"Erro HTTP: {erro}\n")
        return []
    except URLError as erro:
        print(f"Erro de URL: {erro}\n")
        return []
    except ValueError as erro:
        print(f"URL mal escrita ou de tipo desconhecido: {erro}\n")
        return []
    
    try:
        bs_obj = BeautifulSoup(html.read(),"html.parser")
        return bs_obj.find_all('h1')
    except AttributeError as erro:
        print(f"Erro de atributo: {erro}\n")
        return []
    except:
        print(f'Erro do BeautifulSoup: {erro}\n')
        return []

print(get_all_h1("http://gartic.com.br"))
