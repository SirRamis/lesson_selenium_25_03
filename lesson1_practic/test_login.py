import time

USER_NAME = ('xpath', '//*[@id="user-name"]')
PASSWORD = ('xpath', '//*[@id="password"]')
LOGIN = ('xpath', '//*[@id="login-button"]')
TITLE = ('xpath', '//*[@id="header_container"]/div[2]/span')

def test_login(driver):
    driver.get('https://www.saucedemo.com/')
    driver.find_element(*USER_NAME).send_keys('standard_user')
    driver.find_element(*PASSWORD).send_keys('secret_sauce')
    driver.find_element(*LOGIN).click()
    actual_text = driver.find_element(*TITLE).text
    expected_text = "Products"
    assert actual_text == expected_text

    time.sleep(4)
