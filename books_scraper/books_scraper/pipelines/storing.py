import re

import psycopg
from scrapy import Spider

from ..items import BookItem


class StoringPipeline:
    def __init__(self):
        self.conn = psycopg.connect("host='localhost' dbname='postgres' user='postgres' password='postgres' port=5432")

    def process_item(self, item: BookItem, spider: Spider) -> BookItem:
        title_escaped = re.sub(r"'", r"''", item["title"])
        with self.conn.cursor() as cursor:
            query = (
                "INSERT INTO books (title, price, rating, in_stock) "
                f"VALUES ('{title_escaped}', {item['price']}, {item['rating']}, {item['in_stock']});"
            )
            cursor.execute(query)
            self.conn.commit()

        return item
