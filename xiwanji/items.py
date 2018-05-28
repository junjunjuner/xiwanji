# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiwanjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    p_Name = scrapy.Field()
    shop_name = scrapy.Field()
    ProductID = scrapy.Field()
    price = scrapy.Field()
    PreferentialPrice = scrapy.Field()
    CommentCount = scrapy.Field()
    GoodRateShow = scrapy.Field()
    GoodCount = scrapy.Field()
    GeneralCount = scrapy.Field()
    PoorCount = scrapy.Field()
    keyword = scrapy.Field()
    type = scrapy.Field()
    brand = scrapy.Field()
    X_name = scrapy.Field()
    open_method = scrapy.Field()
    laundry = scrapy.Field()
    capacity = scrapy.Field()
    control = scrapy.Field()
    dry_method = scrapy.Field()
    disinfection = scrapy.Field()
    consump = scrapy.Field()
    color = scrapy.Field()
    product_url = scrapy.Field()
    source = scrapy.Field()
    ProgramStarttime = scrapy.Field()
