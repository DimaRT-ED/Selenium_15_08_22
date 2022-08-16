import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def setup():
    print("-----------start setup")
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("-----------end setup")







@pytest.mark.parametrize("user,password", [('Admin', 'admin123'), ('Admin-1', 'admin123'), ('Admin', 'admin123-4'),('Admin-1', 'A--admin123')])
def test_param(user,password):
    print("-----IN   test_param")
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys(user)
    driver.find_element(By.ID, 'txtPassword').send_keys(password)
    driver.find_element(By.ID, 'btnLogin').click()
    time.sleep(7)
    print("2-----End test_param")




