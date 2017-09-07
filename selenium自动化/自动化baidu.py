#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
print('打开百度')
driver.get("http://www.baidu.com")
print('搜索selenium')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("Selenium2")
driver.find_element_by_xpath('//*[@id="su"]').click()
driver.quit()


