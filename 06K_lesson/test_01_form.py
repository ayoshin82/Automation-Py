
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
submit = driver.find_element(By.CSS_SELECTOR, "button.btn")

first_name.send_keys("Иван")
last_name.send_keys("Петров")
address.send_keys("Ленина, 55-3")
email.send_keys("test@skypro.com")
phone_number.send_keys("+7985899998787")
zip_code.clear
city.send_keys("Москва")
country.send_keys("Россия")
job_position.send_keys("QA")
company.send_keys("SkyPro")

submit.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
address = driver.find_element(By.CSS_SELECTOR, "#address")
email = driver.find_element(By.CSS_SELECTOR, "#e-mail")
phone_number = driver.find_element(By.CSS_SELECTOR, "#phone")
zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
city = driver.find_element(By.CSS_SELECTOR, "#city")
country = driver.find_element(By.CSS_SELECTOR, "#country")
job_position = driver.find_element(By.CSS_SELECTOR, "#job-position")
company = driver.find_element(By.CSS_SELECTOR, "#company")

red = zip_code.value_of_css_property("color")
green = first_name.value_of_css_property("color")

assert zip_code.value_of_css_property("color") == red

elements = [
    first_name,
    last_name,
    address,
    email,
    phone_number,
    city,
    country,
    job_position,
    company
    ]

for element in elements:
    assert element.value_of_css_property("color") == green

driver.quit()
