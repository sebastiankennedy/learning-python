import scrapy
import bs4
from ..items import DangdangItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com/']
    start_urls = []

    for i in range(1, 4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(i)
        start_urls.append(url)

    def parse(self, response):
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul', class_='bang_list')
        li_list = ul.find_all('li')
        for li in li_list:
            dangdang = DangdangItem()
            dangdang['name'] = li.find('div', class_='name').find('a')['title']
            dangdang['price'] = li.find('div', class_='price').find('span', class_='price_n').text
            dangdang['author'] = li.find('div', class_='publisher_info').find('a')['title']
            print(dangdang)
            yield dangdang
