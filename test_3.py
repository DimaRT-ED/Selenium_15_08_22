from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield                               # will run on the end of tests
    driver.close()
    driver.quit()

#@pytest.mark.skip
def test_login(setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    title = driver.title
    assert title == 'OrangeHRM'

#@pytest.mark.skip
def test_login2(setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    title = driver.title
    assert title == 'OrangeHRM'