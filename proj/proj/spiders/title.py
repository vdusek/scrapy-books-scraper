import scrapy


class MySpider(scrapy.Spider):

    name = 'my_spider'
    start_urls = ['https://example.com']

    def parse(self, response):
        for link in response.css('a::attr(href)'):
            yield scrapy.Request(link.get(), callback=self.parse)

        item = {}
        item['title'] = response.css('title::text').extract_first()

        yield item
