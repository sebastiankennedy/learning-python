from selenium import webdriver
import time

# 设置驱动
driver = webdriver.Chrome()

# 打开网址
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(3)

# 获取表单并且输入电子邮箱
email_input = driver.find_element_by_id('user_login')
email_input.send_keys('xxx@xxx.com')

# 获取表单并且输入密码
password_input = driver.find_element_by_id('user_pass')
password_input.send_keys('123456')

# 点击登陆按钮
submit_button = driver.find_element_by_id('wp-submit')
submit_button.click()

# 然后跳转页面
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_03')
time.sleep(10)

# 获取评论输入框
comment_input = driver.find_element_by_id('comment')
comment_input.send_keys('Hello World, Sebastian Kennedy, Selenium')

# 点击发表评论
submit_button = driver.find_element_by_id('submit')
submit_button.click()
