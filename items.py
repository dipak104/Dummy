# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InvestopediaItem(scrapy.Item):
	NewsTitle = scrapy.Field()
	story = scrapy.Field()
