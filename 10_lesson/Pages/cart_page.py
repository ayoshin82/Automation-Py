
from selenium.webdriver.common.by import By
import allure

class CartPage:
    def __init__(self, driver):
       self.driver = driver

    @allure.step("Нажатие кнопки 'Checkout'.")

    def in_cart(self):
       self.driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()

    def click_checkout(self):
       self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
