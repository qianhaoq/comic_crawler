from scrawler.items import ComicItem
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
import json

class ComicSpider(Spider):
    name = "comic"
    domain = "wiki.52poke.com"
    allowed_domains = ["wiki.52poke.com","www.google.com","image.baidu.com"]
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
            # item['google_image_url'] = 'https://www.google.com/search?q=' + search + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            # item['google_image_url'] = 'https://www.google.ca/search?source=lnms&tbm=isch&q=' + search
            item['baidu_image_url'] = 'https://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=1&rn=50&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
            # item['image_path'] = ""
            # sub_url = "http://" + item['page_url']

            # print (item['number'])
            # print (item['google_image_url'])
            # yield item
            # if sub_url == self.start_urls[0]:
            #     continue
            # yield item
            # sub_url = item['google_image_url']
            yield Request(item['baidu_image_url'], callback=self.parse_item, meta={'item':item})

    def parse_item(self, response):
        """
        抓取子页面，以补充图片信息
        """
        item = response.meta['item']
        print ('------------------------------')
        print (response.body)
        print ('------------------------------')
        # data = response.xpath('/').extract()[0].strip()
        # page_detail = Selector(response)
        # item['image_urls'] = []
        # rsp_data = json.loads(data)
        # item['image_urls'] = []
        # for image_info in rsp_data['imgs']:
        #     item['image_urls'].append(image_info['objURL'])
        return item
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
        yield item
