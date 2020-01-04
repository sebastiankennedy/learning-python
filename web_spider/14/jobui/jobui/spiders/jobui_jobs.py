import scrapy
import bs4
from ..items import JobuiItem


def parse_job(response):
    bs = bs4.BeautifulSoup(response.text, 'html.parser')
    company = bs.find(id='companyH1').text
    data = bs.find_all('li', class_='company-job-list')
    for datum in data:
        item = JobuiItem()
        item['company_name'] = company
        item['job_title'] = datum.find('a').find('h3').text
        item['address'] = datum.find_all('span')[0]['title']
        item['requirements'] = datum.find_all('span')[1]['title']
        # 使用 yield 语句把 item 返回给引擎
        print(item)
        yield item


class JobuiSpider(scrapy.Spider):
    name = 'jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = soup.find_all('ul', class_="textList flsty cfix")
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['href']
                url = 'https://www.jobui.com{id}jobs'
                format_url = url.format(id=company_id)
                print(format_url)
                # 使用 yield 语句把构造好的 request 对象传递给引擎。
                yield scrapy.Request(format_url, callback=parse_job)
