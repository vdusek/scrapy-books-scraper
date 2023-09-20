from scrapy import Spider

from ..items import BookItem


class CleaningPipeline:

    def process_item(self, item: BookItem, spider: Spider) -> BookItem:
        number_map = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
        }
        return BookItem(
            title=item['title'],
            price=float(item['price'].replace('£', '')),
            rating=number_map[item['rating'].split(' ')[1].lower()],
            in_stock=True if item['in_stock'].lower() == 'in stock' else False,
        )
