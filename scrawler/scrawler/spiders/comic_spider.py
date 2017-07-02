import scrapy
from scrawler.items import ComicItem

class ComicSpider(scrapy.Spider):
    name = "comic"
    domain = "wiki.52poke.com"
    allowed_domains = ["wiki.52poke.com"]
    start_urls = ["http://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88",]
    #rules = [ #define useful url
    #    Rule(sle(allow=("")), follow=True, callback='parse_item')           
 #]
    def parse(self, response):
        domain = "wiki.52poke.com"
        for i in response.xpath("//body//table[@class='a-c roundy eplist bgl-一般 b-一般 bw-2']//tr//td[2]"):
            item = ComicItem()
            item['name'] = i.xpath('a/text()').extract()[0]
            item['url'] = domain + i.xpath('a/@href').extract()[0]
            #print (item['name'])
            yield item