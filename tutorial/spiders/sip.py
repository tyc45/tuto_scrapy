import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# https://sipwhiskey.com/collections/japanese-whisky
# https://sipwhiskey.com/collections/japanese-whisky/products/nikka-coffey-malt-whisky

class SipSpider(CrawlSpider):
    name = 'sip'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['http://sipwhiskey.com/']

    rules = (
        Rule(LinkExtractor(allow='collections/japanese-whisky')),
        Rule(LinkExtractor(allow='products'), callback='parse_item')
    )

    def parse_item(self, response):
        item = {
            'brand':response.css('div.vendor a::text').get(),
            'name':response.css('h1.title::text').get(),
            'price':response.css('span.price::text').get()
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
