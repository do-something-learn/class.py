import scrapy


class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
