# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os
import json
import time


IMAGES_DIR = os.getcwd()
# 图片下载管道
class MyImagePipeline(ImagesPipeline):

    # def file_path(self, request, response=None, info=None):
    # #     """
    # #     :param request: 每一个图片下载管道请求
    # #     :param response:
    # #     :param info:
    # #     :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
    # #     :return: 每套图的分类目录
    # #     """
    #     item = request.meta['item']
    #     folder = item['number']
    #     image_guid = request.url.split('/')[-1]
    #     filename = u'full/{0}/{1}'.format(folder, image_guid)
    #     return filename

    # default_headers = {
    #     'accept': 'image/webp,image/*,*/*;q=0.8',
    #     'accept-encoding': 'gzip, deflate, sdch, br',
    #     'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
    #     'referer': 'https://www.google.com/imghp?hl=zh-CN&tab=wi',
    #     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    # }


    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

            # self.default_headers['referer'] = image_url
            # yield Request(image_url, headers=self.default_headers)

    # def get_media_requests(self, item, info):
    #     for image_url in item['image_urls']:
    #         yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        dir_path = '%s/images/' % (IMAGES_DIR) 
        if not image_paths:
            raise DropItem("Item contains no images")
        # 等待列表
        wait_list = []
        for img_path in image_paths:
            old_img = dir_path + img_path
            new_img = dir_path + item['number'] + '/' + img_path.split('/')[-1]
            if os.path.exists(old_img):
                os.rename(old_img, new_img)
            else:
                wait_list.append(img_path)
        # 等待由于磁盘写入未被处理的图片
        time.sleep(2)
        # 消耗等待列表的数据
        for img_path in wait_list:
            old_img = dir_path + img_path
            new_img = dir_path + item['number'] + '/' + img_path.split('/')[-1]
            if os.path.exists(old_img):
                os.rename(old_img, new_img)
        return item


# item json 存入本地管道
class ScrawlerPipeline(object):

    # def file_path(self, request, response=None, info=None):
    #     """
    #     :param request: 每一个图片下载管道请求
    #     :param response:
    #     :param info:
    #     :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
    #     :return: 每套图的分类目录
    #     """
    #     item = request.meta['item']
    #     folder = item['number']
    #     image_guid = request.url.split('/')[-1]
    #     filename = u'full/{0}/{1}'.format(folder, image_guid)
    #     return filename


    # def get_media_requests(self, item, info):
    #     for image_url in item['image_urls']:
    #         yield Request(image_url)
    #
    # def image_downloaded(self, response, request, info):
    #     try:
    #         super(BkamImagesPipeline, self).image_downloaded(response, request, info)
    #     except:
    #         log.msg(str(ex), level=log.WARNING, spider=info.spider)
    #
    # def item_completed(self, results, item, info):
    #     image_path = [x['path'] for ok, x in results if ok]
    #     if not image_path:
    #         raise DropItem('Item contains no images')
    #         print("error: Item contains no images")
    #     # item['image_paths'] = image_path
    #     return item

    # def __init__(self):

    # 如果spider is open，打开一个文件
    def open_spider(self, spider):
        self.file = open('items.json', 'w+')
        self.IMAGES_DIR = os.getcwd()
    #
    # # 随着spider的关闭，关闭打开的文件
    def close_sipder(self, spider):
        self.file.close()
    #
    # # 处理传过来的item数据
    def process_item(self, item, spider):

        dir_path = '%s/images/' % (self.IMAGES_DIR)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        current_path = dir_path + item['number'] + '/'
        if not os.path.exists(current_path):
            os.makedirs(current_path)

        item['image_dir'] = current_path

        # 资料写入文件
        line = json.dumps(dict(item)).encode().decode('unicode-escape') + "\n"
        self.file.write(line)

        return item
