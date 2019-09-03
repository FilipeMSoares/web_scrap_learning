import scrapy

class Citacoes_Spider3 (scrapy.Spider):
    name = 'citacoes3'
    
    start_urls = ['https://quotes.toscrape.com/page/1',"https://quotes.toscrape.com/page/2"]

    def parse(self, response):
        for citacao in response.css('div.quote'):
            yield {
                "texto": citacao.css('span.text::text').extract()[0],
                "author": citacao.css('small.author::text').extract()[0],
                "tags": citacao.css('div.tags a.tag::text').extract()
            }
