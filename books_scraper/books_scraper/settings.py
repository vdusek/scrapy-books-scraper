BOT_NAME = 'books_scraper'

SPIDER_MODULES = ['books_scraper.spiders']
NEWSPIDER_MODULE = 'books_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {
    'books_scraper.pipelines.cleaning.CleaningPipeline': 100,
    'books_scraper.pipelines.storing.StoringPipeline': 200,
}
