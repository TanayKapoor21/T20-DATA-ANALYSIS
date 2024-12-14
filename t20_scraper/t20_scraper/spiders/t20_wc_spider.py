import scrapy


class T20WcSpiderSpider(scrapy.Spider):
    name = "t20_wc_spider"
    allowed_domains = ["espncricinfo.com"]
    start_urls = ["https://espncricinfo.com"]

    def parse(self, response):
        pass
