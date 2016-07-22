import scrapy
from scrapy.selector import Selector

from bd3.items import Bd3Item

def first(sel, xpath):
    return sel.xpath(xpath).extract_first()

class PrisonSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["digitalspy.com"]
    start_urls = [
        "http://www.digitalspy.com/",
    ]

    def parse(self, response):
	for i in range(0,100):
	    a = str(i)
	    proxima_url = 'http://www.digitalspy.com/landing-feed-news/?template=tv-show&landingTemplate=news&id=150&pageNumber='+a
	    yield scrapy.Request(proxima_url, self.page)

    def page(self, response):
        sites = Selector(response).xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' landing-feed--story ')]") 
        for site in sites:
            item = Bd3Item()
            item['titulo']=site.xpath('.//div/div/div[2]/a/text()').extract(),
	    item['link']=site.xpath('.//div/div/div[2]/a/@href').extract(),
	    item['data']=site.xpath('.//div/div/div[2]/div[2]/time/text()').extract(),
            yield item



