import scrapy

class Citacoes4Spider(scrapy.Spider):
    name = "citacoes4"
    start_urls = [
        "http://quotes.toscrape.com/page/1",
        "http://quotes.toscrape.com/page/2",
        "http://quotes.toscrape.com/page/3",
        "http://quotes.toscrape.com/page/4"
    ]
    def parse(self, response):
        for citacao in response.css('div.quote'):
            yield{
                "texto": citacao.css('span.text::text').extract_first(),
                "autor": citacao.css('small.author::text').extract_first()
            }