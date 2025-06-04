
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    BUTTON_TEMPLATE = "//span[text()='{}']"

    def click_button(self, value):
        self.driver.find_element(By.XPATH, self.BUTTON_TEMPLATE.format(value)).click()

    def __init__(self, driver):
        self.driver = driver
        self.url = (
          "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step("Установка времени задержки {timeout} секунд.")
    def open(self):
        self.driver.get(self.url)

    def setting_the_delay(self):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Нажатие кнопок.")
    def get_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def check_result(self):
        WebDriverWait(self.driver, 46).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".screen"
                     ), "15"))

        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Результат не равен 15, а равен {result}"
        return result
