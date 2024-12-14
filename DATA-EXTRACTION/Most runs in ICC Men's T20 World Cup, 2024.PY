import scrapy

class T20WcSpider(scrapy.Spider):
    name = 't20_wc_spider'
    allowed_domains = ['espncricinfo.com']
    start_urls = ['https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946']

    def parse(self, response):
        headers = response.css('thead tr th::text').getall()
        rows = response.css('tbody tr')
        
        data = []
        for row in rows:
            values = row.css('td::text').getall()
            data.append(dict(zip(headers, values)))

        # Save the data to a JSON file
        with open('t20_world_cup_batting_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        self.log('Data has been saved to t20_world_cup_batting_data.json')
