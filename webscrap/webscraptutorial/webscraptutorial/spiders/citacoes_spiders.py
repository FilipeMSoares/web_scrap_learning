import scrapy

class SpiderCitacoes(scrapy.Spider):
    name = 'citacoes'

    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        numero_da_pagina = response.url.split("/")[-2]
        nome_arquivo = f'citacoes-{numero_da_pagina}.html'
        with open(nome_arquivo,"wb") as f:
            f.write(response.body)
        
        self.log(f"Arquivo salvo {nome_arquivo}")