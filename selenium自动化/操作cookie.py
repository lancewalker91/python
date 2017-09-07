from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.yunke.com')
cookie = driver.get_cookies()
print(cookie)
driver.quit()

