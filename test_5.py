import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(params=["a1","a2"])
def demo_fixture(request):
    print("-----IN   demo_fixture")
    print(request.param)
    print("-----END   demo_fixture")


def test_param(demo_fixture):
    print("-----IN   test_param")



"""
# @pytest.mark.skip
def test_login2(setup):
    print("2-----Start test_login2")
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    title = driver.title
    assert title == 'OrangeHRM'
    print("2-----End test_login2")



@pytest.yield_fixture()  # executes specific method before_&_after every test method
def setup():
    print("2-----Start setup")
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("2-----End setup")
    yield
    print("2-----Start yield_part")
    driver.close()
    driver.quit()
    print("2-----End yield_part")
"""
