# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MilpyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    ref_num = scrapy.Field()
    location = scrapy.Field()
    seller = scrapy.Field()
    color = scrapy.Field()
    door_num = scrapy.Field()
    fuel_type = scrapy.Field()
    hp = scrapy.Field()
    mileage = scrapy.Field()
    transmission = scrapy.Field()
    year = scrapy.Field()
