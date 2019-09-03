import scrapy

class Citacoes_Till_The_End (scrapy.Spider):
    name = "citacoes_till_the_end"

    start_urls = [ "http://quotes.toscrape.com" ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield{
                'texto' : quote.css("span.text::text").extract_first(),
                'autor': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags a.tag::text").extract_first()
            }
            pagina = response.url.split("/")[-2]
            nome_arquivo = f'citacoes-{pagina}.html'
            with open(nome_arquivo, 'wb') as f:
                f.write(response.body)
            next_page = response.css('li.next a::attr(href)').extract_first()
            if(next_page is not None):
                #next_page = response.urljoin(next_page)
                yield response.follow(href=next_page,callback=self.parse)
            #ou
            #for next_page in response.css('li.next a::attr(href)')
                #yield response.follow(href=next_page,callback=self.parse)
