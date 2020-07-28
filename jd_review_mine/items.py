# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdReviewMineItem(scrapy.Item):
    sku = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()
    content = scrapy.Field()
    score = scrapy.Field()
    plus = scrapy.Field()
    nickname = scrapy.Field()
    creationTime = scrapy.Field()





