import bs4
import requests
import openpyxl

movies = []

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em', class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span', class_="rating_num").text
        url_movie = titles.find('a')['href']

        tes = ''
        if titles.find('span', class_="inq") != None:
            tes = titles.find('span', class_="inq").text
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie)
        else:
            print(num + '.' + title + '——' + comment + '\n' + '\n' + url_movie)

        movies.append([
            num,
            title,
            comment,
            url_movie,
            tes
        ])

if movies:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '豆瓣电影 Top 250'
    sheet['A1'] = '序号'
    sheet['B1'] = '电影'
    sheet['C1'] = '评分'
    sheet['D1'] = '推荐语'
    sheet['E1'] = '链接'

    for movie in movies:
        sheet.append(movie)
    wb.save('top250movies.xlsx')
