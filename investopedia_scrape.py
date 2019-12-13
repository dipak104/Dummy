import scrapy
from investopedia.items import InvestopediaItem
from datetime import datetime
import re


class Investopedia(scrapy.Spider):
	name = "my_scraper"

	# First Start Url
	start_urls = ["https://www.investopedia.com/markets-news-4427704"]


	
	def parse(self, response):
			for href in response.xpath("//li[contains(@class, 'comp card-list__item mntl-block')]//@href"):
					# add the scheme, eg http://
					url  = href.extract() 
					yield scrapy.Request(url, callback=self.parse_dir_contents)	
					
	def parse_dir_contents(self, response):
		item = InvestopediaItem()

		# Getting Campaign Title
		item['NewsTitle'] = response.xpath("//h1[contains(@id, 'article-heading_2-0')]/descendant::text()").extract()[0].strip()

		# Getting Story
		story_list = response.xpath("//div[contains(@id, 'article-body_1-0')]/descendant::text()").extract()
		story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
		item['story']  = " ".join(story_list)


		yield item
