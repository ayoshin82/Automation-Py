
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Авторизация с логином {username} и паролем {password}")

    def authorization(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "#user-name"))
        ).send_keys("standard_user")

        self.driver.find_element(
            By.CSS_SELECTOR, "#password"
        ).send_keys("secret_sauce")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
