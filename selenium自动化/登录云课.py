from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.yunke.com/index.main.login')
driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[1]/div[2]/input').send_keys('17600117243')
driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[2]/input').clear()
driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[2]/input').send_keys('117243')
driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[4]/input').click()
driver.get('https://www.yunke.com')
a = driver.find_element_by_xpath('//*[@id="topnav"]/div/ul/li[3]/a')
ActionChains(driver).move_to_element(a).perform()
driver.find_element_by_xpath('//*[@id="topnav"]/div/ul/li[3]/div/div/a[1]').click()
driver.get('https://litao.yunke.com/org')
driver.find_element_by_xpath('html/body/section/div/div/div[1]/ul/li[3]/a').click()
driver.get('https://litao.yunke.com/user.org.course')
driver.find_element_by_xpath('html/body/section[1]/div/div/div[2]/ul/li[2]/div[5]/p[2]/a/span[2]').click()
driver.get('https://litao.yunke.com/org.course.plan.44349')
# driver.find_element_by_xpath(".//*[@id='updateBtn-plan-edit']").click()
#driver.find_element_by_id('updateBtn-plan-edit').click()
driver.find_element_by_link_text('删除班级').click()
