import scrapy
from scrapy.selector import Selector
from datetime import datetime
from bd3.items import Bd3Item

now = datetime.now()
def first(sel, xpath):
    return sel.xpath(xpath).extract_first()

class Youtube_pb(scrapy.Spider):
    name = 'bd3'
    youtube_channel = 'series prison break'
    start_urls = ['https://www.youtube.com/results?search_query=%s' % youtube_channel]

    def parse(self, response):
	for i in range(0,10000):
	    a = str(i)
	    proxima_url = 'https://www.youtube.com/results?search_query=prison+break&page='+a
	    yield scrapy.Request(proxima_url, self.page)

    def page(self, response):
        for sel in  Selector(response).xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' item-section ')]/li"):
	    item = Bd3Item()
            item['link'] = response.urljoin(first(sel, './/h3/a/@href')),
            item['titulo'] = first(sel, './/h3/a/text()'),
	    item['data_postagem'] = first(sel, ".//ul/li[1]/text()"),
            item['visualizacoes'] = first(sel, ".//ul/li[2]/text()"),
	    item['data_coleta'] = now
            yield item
