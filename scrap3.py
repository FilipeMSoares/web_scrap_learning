import urllib.request as request
from bs4 import BeautifulSoup
import re

paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def abrir_pagina(url_da_pagina,regex):
    global paginas
    global paginas_invalidas
    print(url_da_pagina)
    try:
        if url_da_pagina not in paginas_invalidas:
            html = request.urlopen(url_da_pagina)
            bsObj = BeautifulSoup(html,"html.parser")

            print("---")
            for link in bsObj.find_all("a",href=re.compile(regex)):
                if "href" in link.attrs:
                    nova_pagina = link.attrs['href']
                    print(nova_pagina)
                    if nova_pagina not in paginas:
                        paginas.add(nova_pagina)
                        abrir_pagina(nova_pagina,regex)
    except:
        print("--->ERRO!")
        paginas_invalidas.add(url_da_pagina)
print("abrir pagina...")
abrir_pagina("http://globoesporte.globo.com",(r".santos."))