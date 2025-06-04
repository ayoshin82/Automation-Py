
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.form_page import FormPage
import allure


@allure.title("Автотест на заполнение формы")
@allure.description("Заполнение некоторых полей значениями и проверка \
                     окрашивания заполненных и незаполненных полей.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.TRIVIAL)


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

    form_page.submit_form()
    form_page.color_check_red()
    form_page.color_check_green()
    driver.quit()
