# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

class ScrawlerPipeline(object):
	def __init__(self):
		self.file = open('items.json', 'w+')
		self.IMAGES_DIR = os.getcwd()

	def process_item(self, item, spider):

		dir_path = '%s/images/' % (self.IMAGES_DIR)

		if not os.path.exists(dir_path):
			os.makedirs(dir_path)

		# 资料写入文件
		line = json.dumps(dict(item)).encode().decode('unicode-escape') + "\n"
		self.file.write(line)

		# 图片下载到本地
		file_path = dir_path + item['number'] + '.png'
		urllib.request.urlretrieve(item['image_url'], file_path)

		return item
