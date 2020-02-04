from selenium import webdriver
import time
import bs4

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher_input = driver.find_element_by_id('teacher')
teacher_input.send_keys('吴枫')

assistant_input = driver.find_element_by_id('assistant')
assistant_input.send_keys('酱酱')

submit_button = driver.find_element_by_class_name('sub')
submit_button.click()
time.sleep(2)

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
content_list = soup.find_all(class_='content')
for content in content_list:
    print(content)
