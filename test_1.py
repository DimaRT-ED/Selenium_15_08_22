from selenium import webdriver
from selenium.webdriver.common.by import By

print("-----------start file test_1")
driver = webdriver.Chrome("C:/Users/sharo/Drivers/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.set_page_load_timeout(5)

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.delete_all_cookies()

driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID , 'txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()
assert driver.title == 'OrangeHRM'

driver.close()
driver.quit()


print("------------end file test_1")