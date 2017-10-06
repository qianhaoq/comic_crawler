# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

class ScrawlerPipeline(object):
	# def __init__(self):

	# 如果spider is open，打开一个文件
	def open_spider(self, spider):
		self.file = open('items.json', 'w+')
		self.IMAGES_DIR = os.getcwd()

	# 随着spider的关闭，关闭打开的文件
	def close_sipder(self, spider):
		self.file.close()

	# 处理传过来的item数据
	def process_item(self, item, spider):

		dir_path = '%s/images/' % (self.IMAGES_DIR)

		if not os.path.exists(dir_path):
			os.makedirs(dir_path)

		current_path = dir_path + item['number'] + '/'
		if not os.path.exists(current_path):
			os.makedirs(current_path)
			
		item['image_dir'] = current_path
		# 图片下载到本地
		# file_path = dir_path + item['number'] + '.png'
		# urllib.request.urlretrieve(item['image_url'], file_path)

		# item['image_path'] = file_path

		# 资料写入文件
		line = json.dumps(dict(item)).encode().decode('unicode-escape') + "\n"
		self.file.write(line)

		return item
