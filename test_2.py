import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#@pytest.mark.skip
def test_login():
    print("-----------start test_login")
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    title = driver.title
    assert title == 'OrangeHRM'
    print("-----------end test_login ")

#@pytest.mark.skip
def test_11():
    print("-----------start test_11")
    driver.get('https://rt-ed.co.il/')
    print("-----------end test_11")

@pytest.mark.tryfirst
def setup():
    print("-----------start setup")
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("-----------end setup")

@pytest.mark.trylast
def teardown():
    print("-----------start teardown")
    driver.close()
    driver.quit()
    print("-----------end teardown")
