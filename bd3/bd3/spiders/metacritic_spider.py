import scrapy
from scrapy.selector import Selector
from bd3.items import Bd3Item

def first(sel, xpath):
    return sel.xpath(xpath).extract_first()

class Metacritic(scrapy.Spider):
    name = 'meta'
    start_urls = ['http://www.metacritic.com/tv/prison-break/user-reviews']

    def parse(self, response):
	for i in range(0,5):
	    a = str(i)
	    proxima_url = 'http://www.metacritic.com/tv/prison-break/user-reviews?page='+a
	    yield scrapy.Request(proxima_url, self.page)

    def page(self, response):
        for sel in  Selector(response).xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' reviews user_reviews ')]/li"):
    	    item = Bd3Item()
            item['autor'] = first(sel, ".//div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/span/text()"),
	    item['data'] = first(sel, ".//div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/text()"),
	    item['nota'] = first(sel, ".//div/div/div/div/div/div[1]/div[1]/div[2]/div/text()"),
	    item['avaliacao'] = first(sel, ".//div/div/div/div/div/div[1]/div[2]/span/text()"),
            yield item


