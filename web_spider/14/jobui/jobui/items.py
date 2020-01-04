# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # 公司名称
    company_name = scrapy.Field()
    # 职位名称
    job_title = scrapy.Field()
    # 公司地址
    address = scrapy.Field()
    # 招聘要求
    requirements = scrapy.Field()
    pass
