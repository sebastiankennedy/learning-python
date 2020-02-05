import bs4
from gevent import monkey

monkey.patch_all()

import gevent, time, requests, csv
from gevent.queue import Queue

start_time = time.time()

movies = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

url_list = ['http://www.mtime.com/top/tv/top100/index.html']
for i in range(2, 11):
    url_list.append('http://www.mtime.com/top/tv/top100/index-' + str(i) + '.html')

work = Queue()
for url in url_list:
    work.put_nowait(url)


def crawler():
    while not work.empty():
        url = work.get_nowait()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            soup = bs4.BeautifulSoup(html, 'html.parser')
            ul = soup.find(id='asyncRatingRegion')
            li_list = ul.find_all('li')
            for li in li_list:
                p_list = li.find_all('p')

                description = ''
                if len(p_list) >= 3:
                    description = p_list[2].text

                movies.append([
                    li.find('h2').get_text(),
                    p_list[0].get_text(),
                    p_list[1].get_text(),
                    description
                ])


task_list = []
for t in range(4):
    task = gevent.spawn(crawler)
    task_list.append(task)

gevent.joinall(task_list)

file = open('movies.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerows(movies)
file.close()

print(time.time() - start_time)
print(len(movies))
