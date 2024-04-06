
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CartFunctionality:

    @classmethod
    def setup_class(cls):
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def login(self):
        self.browser.get('https://www.saucedemo.com/')
        self.browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
        self.browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    def add_item_to_cart(self):
        self.browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()
        time.sleep(2)

    def remove_item_from_cart(self):
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()
        time.sleep(2)

    def test_added_item_in_cart(self):
        self.login()
        self.add_item_to_cart()
        assert self.browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине нет товаров'

    def test_delete_item_in_cart(self):
        self.login()
        #self.add_item_to_cart()
        self.remove_item_from_cart()
        assert self.browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'
