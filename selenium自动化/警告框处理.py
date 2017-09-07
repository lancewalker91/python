from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)
driver.switch_to_alert().accept()
driver.quit()

