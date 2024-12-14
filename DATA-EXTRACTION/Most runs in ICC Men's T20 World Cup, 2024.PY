import scrapy
import json

class T20WorldCupBattingSpider(scrapy.Spider):
    name = 't20_world_cup_batting'
    allowed_domains = ['espncricinfo.com']
    start_urls = ['https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946']

    def parse(self, response):
        table_headers = response.css('thead tr th::text').getall()

        for row in response.css('tbody tr'):
            player_data = dict(zip(table_headers, row.css('td::text').getall()))
            yield player_data