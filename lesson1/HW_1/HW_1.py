from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest, time


browser = webdriver.Chrome()

def test_auth_positive_2():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Не прошел тест'

    time.sleep(3)
    browser.quit()

def test_auth_negativ():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'Не прошел тест'

    browser.quit()

def test3_add_item():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

    assert browser.find_elements(By.XPATH,'//*[@id="shopping_cart_container"]/a/span'), 'В корзине нет товаров'

    time.sleep(2)
    browser.quit()

    # product = browser.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    # assert product is not None, 'count of products does not correspond to added'

def test4_deleit_item():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click() #Удаляет с корзины

    assert not browser.find_elements(By.XPATH,'//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'

    time.sleep(4)
    browser.quit()


def test5_added_item_in_cart():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click() # Логинится
    browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()# Проходит в карточку
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()# Добавляет в карзину из карточки
    time.sleep(2)

    assert browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине нет товаров'

    time.sleep(4)
    browser.quit()

def test6_deleit_item_in_cart():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click() # Логинится
    browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()# Проходит в карточку
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()# Добавляет в карзину из карточки
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Удаляет с корзины через карточку товара

    assert not browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'

    time.sleep(4)
    browser.quit()