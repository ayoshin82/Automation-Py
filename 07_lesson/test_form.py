from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage
from time import sleep



def test_01_form():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(
        ).install()))
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form(
        'Иван', 'Петров', 'Ленина, 55-3',
        'test@skypro.com', '+7985899998787',
        'Москва', 'Россия', 'QA',
        'SkyPro')

    #sleep(5)
    form_page.submit_form()
    form_page.color_check_red()
    form_page.color_check_green()
    #sleep(2)
    driver.quit()