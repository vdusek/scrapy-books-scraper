from urllib.parse import urljoin

import scrapy


class BookSpider(scrapy.Spider):

    name = 'book_spider'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        yield {
            'url': response.url.strip(),
            'title': response.css('title::text').extract_first().strip(),
        }

        # for link_href in response.css('a::attr("href")'):
        #     link_url = urljoin(response.url, link_href.get())
        #     if link_url.startswith(('http://', 'https://')):
        #         yield scrapy.Request(link_url)
