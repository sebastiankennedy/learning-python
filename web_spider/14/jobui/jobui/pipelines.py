# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class JobuiPipeline(object):
    def __init__(self):
        # 创建工作簿
        self.wb = openpyxl.Workbook()
        # 定位活动表
        self.ws = self.wb.active
        # 添加表头部
        self.ws.append(['公司', '职位', '地址', '招聘信息'])

    # 默认处理 item 方法
    def process_item(self, item, spider):
        line = [
            item['company_name'],
            item['job_title'],
            item['address'],
            item['requirements'],
        ]
        self.ws.append(line)

        # 返回 item 至引擎
        return item

    # 爬虫结束时，回调此方法
    def close_spider(self, spider):
        self.wb.save('./johui.xlsx')
        self.wb.close()
