from scrawler.items import ComicItem
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

class ComicSpider(Spider):
    name = "comic"
    allowed_domains = ["wiki.52poke.com"]
    start_urls = ["http://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88",]

    def parse(self, response):
        """
        抓取list页面
        """
        domain = "wiki.52poke.com"
        for i in response.xpath("//body//table[@class='a-c roundy eplist bgl-一般 b-一般 bw-2']//tr[position()>3]"):
            item = ComicItem()
            no = i.xpath('td[1]/text()').extract()[0]
            if (len(no) < 4):
                continue
            item['number'] = no[2:5]
            print ("number = " + item['number'])
            item['name_cn'] = i.xpath('td[2]/a/text()').extract()[0]
            item['name_en'] = i.xpath('td[4]/a/text()').extract()[0]
            item['page_url'] = domain + i.xpath('td[2]/a/@href').extract()[0]
            yield item

            #yield Request(item['page_url'], callback=self.sub_parse, meta={'item':item})

    # def sub_parse(self, response):
    #     """
    #     抓取子页面，以补充图片信息
    #     """
    #     item = response.meta['item']

    #     #page_detail = Selector(response)

    #     item['image_url'] = response.xpath("//body//div[@id='content']//img[@alt=" + item[''])
