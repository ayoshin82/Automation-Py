
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


waiter = WebDriverWait(driver, 10)


driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

driver.find_element(By.CSS_SELECTOR, "#password").clear()
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

driver.find_element(
    By.CSS_SELECTOR, "#shopping_cart_container").click()

driver.find_element(
    By.CSS_SELECTOR, "#checkout").click()


driver.find_element(By.CSS_SELECTOR, "#first-name").clear()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Kitia")

driver.find_element(By.CSS_SELECTOR, "#last-name").clear()
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Visli")

driver.find_element(By.CSS_SELECTOR, "#postal-code").clear()
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(199406)

driver.find_element(By.CSS_SELECTOR, "#continue").click()

total = list(
    (driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text).split(" ")
    )

assert total[1] == "$58.29"

print(total)

waiter.until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#continue"), "58.29")
 )

driver.find_element(By.CSS_SELECTOR, "#finish").click()

driver.quit()
