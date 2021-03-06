# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
	# 动漫人物唯一id
	id = scrapy.Field()
	# 动漫名称
	comic_name = scrapy.Field()
	# 动漫人物编号
	number = scrapy.Field()
	# 动漫人物中文名
	name_cn = scrapy.Field()
	# 动漫人物日文名
	name_jp = scrapy.Field()
	# 动漫人物英文名
	name_en = scrapy.Field()
	# 动漫人物主页url
	page_url = scrapy.Field()
	# img_url标准图片地址
	img_url = scrapy.Field()
	# 本地图片地址
	local_img_path = scrapy.Field()
	# # google搜索页面url
	# google_image_url = scrapy.Field()
	# # 百度图片搜索结果页面
	# baidu_image_url = scrapy.Field()
	# google picture url
	# image_urls = scrapy.Field()
	# 本地图片保持路径
	# image_dir = scrapy.Field()
	#image_url = scrapy.Field()
	#image_path = scrapy.Field()
	# image_paths = scrapy.Field()
