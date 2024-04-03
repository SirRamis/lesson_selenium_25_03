from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

USER_NAME = ('xpath', '//*[@id="user-name"]')
def test_auth_positive():
    browser = webdriver.Chrome()
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element(*USER_NAME).send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html','Не прошел тест'

    browser.quit()

    #assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', "Элемент не выбран"
