# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class ScrawlerPipeline(object):

	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield Request(image_url)

	def item_completed(self, results, item, info):
		image_path = [x['path'] for ok, x in results if ok]
		print (image_path)
		if not image_path:
			raise DropItem('Item contains no images')
			# print("error: Item contains no images")
		item['image_paths'] = image_path
		return item
	"""
	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield scrapy.Request(image_url)

	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			print("error: Item contains no images")
		item['image_paths'] = image_paths
		return item
	"""
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

		# for image_url in item['image_urls']:
		# 	unit_name = image_url.split('/')[-1]
		# 	image_name = item['image_dir'] + unit_name
		# 	with open(image_name, 'wb') as handle:
		# 		reponse = requests.get(image_url, stream=True)
		# 		for block in response.iter_content(1204):
		# 			if not block:
		# 				break
		# 			handle.write(block)

		return item
