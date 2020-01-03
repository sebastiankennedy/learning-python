import scrapy
import bs4
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    # 定义爬虫的唯一标识
    name = 'douban'

    # 允许爬虫爬取的网址域名
    allowed_domains = ['book.douban.com']

    # 设置爬虫需要爬取的网址
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        tr_list = bs.find_all('tr', class_='item')
        for data in tr_list:
            item = DoubanItem()
            item['title'] = data.find_all('a')[1]['title']
            item['score'] = data.find('span', class_='rating_nums').text
            item['publish'] = data.find('p', class_='pl').text
            print(item['title'])
            # yield 类似 return，但它不会结束函数，并且能够返回多次信息
            yield item
