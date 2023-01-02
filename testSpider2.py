import scrapy


class Testspider2Spider(scrapy.Spider):
    name = 'testSpider2'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
