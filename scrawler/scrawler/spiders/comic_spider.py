from scrawler.items import ComicItem
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
import json
import re
import os
import random
import time

class ComicSpider(Spider):
    name = "comic"
    domain = "wiki.52poke.com"
    allowed_domains = ["wiki.52poke.com","www.google.ca","image.baidu.com"]
    start_urls = ["http://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88",]

    def parse(self, response):
        """
        抓取list页面
        """
        for i in response.xpath("//body//table[@class='a-c roundy eplist bgl-一般 b-一般 bw-2']//tr[position()>3]"):
            item = ComicItem()
            no = i.xpath('td[1]/text()').extract()[0]
            if (len(no) < 4):
                continue
            item['comic_name'] = "Pokemon"
            item['number'] = no[2:5]
            item['name_cn'] = i.xpath('td[2]/a/text()').extract()[0]
            item['name_jp'] = i.xpath('td[3]/a/text()').extract()[0]
            item['name_en'] = i.xpath('td[4]/a/text()').extract()[0]
            item['page_url'] = self.domain + i.xpath('td[2]/a/@href').extract()[0]

            # 补充google搜索结果页面
            keyword = item['name_en']
            search = keyword.replace(' ', '%20')

            item['google_image_url'] = 'https://www.google.ca/search?q=' + search + '&ie=UTF-8&tbm=isch'

            for i in range(0, 1):
                input_url = item['google_image_url'] + '&start=' + str(20 * i) + '&sa=N'
                t = random.randint(0, 10) * 0.1
                time.sleep(t)
                yield Request(input_url, callback=self.google_parse_item, meta = {'item' : item, 'dont_redirect': True, 'handle_httpstatus_list': [302]})
                
                


            # item['google_image_url'] = 'https://www.google.ca/search?source=lnms&tbm=isch&q=' + search

            # item['google_image_url'] =  'https://www.google.ca/search?q=' + search + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            # item['baidu_image_url'] = 'https://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=1&rn=50&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
            # yield Request(item['baidu_image_url'], callback=self.baidu_parse_item, meta={'item':item})


    def google_parse_item(self, response):
        """
        抓取google图片搜素结果的子页面图片链接
        """
        item = response.meta['item']

        item['image_urls'] = []

        

        ## old version
        for i in response.xpath("//*[@id='ires']/table"):
            for sub_url in i.xpath("//tr/td/a/img/@src").extract():
                item['image_urls'].append(sub_url)
        yield item



    def baidu_parse_item(self, response):
        """
        抓取baidu图片的子页面，以补充图片信息
        """
        item = response.meta['item']
        item['image_urls'] = []
        raw_data = response.body.decode('utf-8')
        rsp_data = json.loads(raw_data)
        image_list = []
        for image_info in rsp_data['imgs']:
            item['image_urls'].append(image_info['objURL'])
        yield item
        # try:
        #     raw_data = response.body.decode('utf-8')
        # except:
        #     return item
        # try:
        #     raw_data = response.body.decode('utf-8')
        # except Exception:
        #     raw_data = response.body.decode('unicode_escape')
        # sub_data = re.sub(r"\\x26([a-zA-Z]{2,6});", r"&\1;", raw_data);
        # sub_data = repair(raw_data)
        # try:
        #     data = json.loads(raw_data)
        # except:
        #     return item
        # for image_info in data['imgs']:
        #     continue
        #     #print(image_info['objURL'])
        #     item['image_urls'].append(image_info['objURL'])
        # data = response.xpath('/').extract()[0].strip()
        # page_detail = Selector(response)
        # item['image_urls'] = []
        # rsp_data = json.loads(data)
        # item['image_urls'] = []
        # for image_info in rsp_data['imgs']:
        #     item['image_urls'].append(image_info['objURL'])
        # return item
            #try:
            #    item['image_urls'].append(i.xpath('li[1]/div[1]/a/img/@src').extract()[0])
            #except Exception:
            #    item['image_urls'].append(i.xpath('li[1]/div/a/img/@src').extract()[0])
        # for i in range(1,51):
            # print ('//[@id="imgid"]/div/ul/li[' + str(i) + ']/div/a/img/@src')
            # //*[@id="imgid"]/div/ul/li[3]/div[1]/a/img
            # //*[@id="imgid"]/div/ul/li[2]/div/a/img
            # //*[@id="imgid"]/div/ul/li[3]/div[1]/a/img
            # //*[@id="imgid"]/div/ul/li[2]/div/a/img
            # item['image_urls'].append(page_detail.xpath('//*[@id="imgid"]/div/ul/li[' + str(i) + ']/div[1]/a/img/@src'))

        # for i in  range(1,51):
        #     item['image_urls'] = response.xpath('//[@id="rg_s"]/div[' + i + ']/a/img/@src')

        # 特殊case ，存在性别差异而图片不同的情况
        # try:
        #     item['image_url'] = "http:" + page_detail.xpath('//body//img[@alt=' + '"' + item['number'] + item['name_en'] + '.png' + '"]/@data-url').extract()[0]
        # except Exception:
        #     item['image_url'] = "http:" + page_detail.xpath('//body//img[@alt=' + '"' + item['number'] + item['name_en'] + '-Male' + '.png' + '"]/@data-url').extract()[0]
        # item['image_url'] = "http:" + page_detail.xpath('//body//img[@width>"240"]/@data-url').extract()[0]
        # try:
        #     item['image_url'] = "http:" + page_detail.xpath('//body//img[@width>"240"]/@data-url').extract()[0]
        # except Exception:
        #     item['image_url'] = "http:" + page_detail.xpath('//body//img[@width="300"]/@data-url').extract()[0]
        # yield item
