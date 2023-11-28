BOT_NAME = 'booksscraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['booksscraper.spiders']
NEWSPIDER_MODULE = 'booksscraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {
    'booksscraper.pipelines.cleaning.CleaningPipeline': 100,
    # 'booksscraper.pipelines.storing.StoringPipeline': 200,
}