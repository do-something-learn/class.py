import scrapy


class Testspider1Spider(scrapy.Spider):
    name = 'testSpider1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
