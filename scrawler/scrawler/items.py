# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
	number = scrapy.Field()
	name_cn = scrapy.Field()
	name_jp = scrapy.Field()
	name_en = scrapy.Field()
	page_url = scrapy.Field()
	google_image_url = scrapy.Field()
	image_dir = scrapy.Field()
	#image_url = scrapy.Field()
	#image_path = scrapy.Field()
