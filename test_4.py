from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestFirst:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        driver.find_element(By.ID, 'btnLogin').click()
        title = driver.title
        assert title == 'OrangeHRM'

    def test_login2(self, test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        driver.find_element(By.ID, 'btnLogin').click()
        title = driver.title
        assert title == 'OrangeHRM'

