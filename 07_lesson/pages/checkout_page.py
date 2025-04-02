
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
       self.driver.find_element(
        By.CSS_SELECTOR, "#first-name"
        ).send_keys(first_name)
       self.driver.find_element(
        By.CSS_SELECTOR, "#last-name"
        ).send_keys(last_name)
       self.driver.find_element(
        By.CSS_SELECTOR, "#postal-code"
        ).send_keys(postal_code)
       self.driver.find_element(
        By.CSS_SELECTOR, "#continue"
        ).click()

    def checking_total_amount(self):
        # Проверка итоговой суммы:
        total = (
            WebDriverWait(self.driver, 10)
            .until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".summary_total_label")))
            .text)
        assert total == "Total: $58.29", (
            f"Итоговая сумма не равна $58.29. " f"Фактическая сумма: {total}")

