
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 45)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(15)
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

final_res = int(driver.find_element(By.CSS_SELECTOR, "div.screen").text)

print("7+8 =", final_res)

assert final_res == 7+8

driver.quit()
