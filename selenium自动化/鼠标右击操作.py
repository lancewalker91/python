from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get('https://www.yunke.com')
right_click = driver.find_element_by_xpath('//*[@id="site_nav"]/li[5]/a')
above = driver.find_element_by_xpath('//*[@id="nav"]/div/div[1]/div/ul[1]/li[2]')
double_click = driver.find_element_by_id('search_btn')
ActionChains(driver).context_click(right_click).perform()
ActionChains(driver).move_to_element(above).perform()
ActionChains(driver).double_click(double_click).perform()
