from selenium import webdriver
from selenium.webdriver.common.by import By


def test_setup():
    print("-----------start  test_setup")
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("------------end test_setup")


def test_login():
    print("-----------start  test_login")
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    assert driver.title == 'OrangeHRM'
    print("------------end test_login")


def test_teardown():
    print("-----------start  test_teardown")
    driver.close()
    driver.quit()
    print("------------end test_teardown")


"""

def test_c():
    print("-----------start  test_c")
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()
    driver.delete_all_cookies()

    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    assert driver.title == 'OrangeHRM'
    print("------------end test_c")


def test_close_driver():
    print("-----------start  test_close_driver")
    driver.close()
    driver.quit()
    print("------------end  test_close_driver")

"""