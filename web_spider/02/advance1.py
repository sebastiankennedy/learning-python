import requests
import bs4

response = requests.get('http://books.toscrape.com/')
print(response.status_code)
if response.status_code == 200:
    html = response.content
    soup = bs4.BeautifulSoup(html, 'html.parser')

    ul = soup.find('ul', class_='nav-list')
    ul = ul.find('ul')
    li = ul.find_all('li')

    for item in li:
        print(item.get_text('|', strip=True))
else:
    print('Something Wrong.')

response = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
if response.status_code == 200:
    html = response.content
    soup = bs4.BeautifulSoup(html, 'html.parser')

    ol = soup.find('ol', class_='row')
    li = ol.find_all('li')
    for item in li:
        name = item.find('h3').find('a')['title']
        price = item.find('p', class_='price_color').text
        rating = item.find('p', class_='star-rating')['class'][1]
        print([name, price, rating])
