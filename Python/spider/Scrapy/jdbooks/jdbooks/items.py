# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #评论数
    # pdnum = scrapy.Field()
    #频道1
    pd1 = scrapy.Field()
    #频道2
    pd2 = scrapy.Field()
    #图书名
    name = scrapy.Field()
    #价格
    price = scrapy.Field()
    #评论数
    cnum = scrapy.Field()
    #作者
    author = scrapy.Field()
    #出版社
    pub = scrapy.Field()
    #店家
    seller = scrapy.Field()



