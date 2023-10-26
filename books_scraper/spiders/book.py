from typing import Generator

from scrapy import Spider
from scrapy.responsetypes import Response

from ..items import BookItem


class BookSpider(Spider):
    name = "book_spider"
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response: Response) -> Generator[BookItem | Response, None, None]:
        self.logger.info(f"BookSpider is parsing {response}...")
        articles = response.css("article.product_pod")

        for article in articles:
            yield BookItem(
                title=article.css("h3 > a::attr(title)").get().strip(),
                price=article.css(".price_color::text").get().strip(),
                rating=article.css(".star-rating::attr(class)").get().strip(),
                in_stock=article.css(".instock.availability::text").getall()[1].strip(),
            )

        next_page_link = response.css("li.next a::attr(href)").extract_first()
        if next_page_link:
            yield response.follow(next_page_link)
