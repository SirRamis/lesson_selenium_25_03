from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/inventory.html')

browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

assert browser.find_elements(By.XPATH,'//*[@id="cart_contents_container"]/div/div[1]/div[4]'), 'В корзине нет товаров'

browser.quit()



# @pytest.fixture(autouse=True)
# def teardown():
#     # Этот код будет выполняться после каждого тестового метода
#     print("\nЭтот код будет выполняться после каждого тестового метода")
#
# def test_example_1():
#     assert True
#
# def test_example_2():
#     assert True
