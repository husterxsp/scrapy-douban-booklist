# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    tag_name = scrapy.Field()
    sub_tag_name = scrapy.Field()
    book_id = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    comment_num = scrapy.Field()
    
    # """docstring for quoteItem"""
    # def __init__(self, arg):
    #     super(quoteItem, self).__init__()
    #     self.arg = arg
        