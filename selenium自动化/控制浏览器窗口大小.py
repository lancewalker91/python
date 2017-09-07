from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
print("设置浏览器480,高800显示")
driver.set_window_size(480,800)
driver.refresh()
driver.quit()
