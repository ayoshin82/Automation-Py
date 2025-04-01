
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop_page import ShopPage


def test_shop_page():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(

        ).install()))
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.authorization()
    shop_page.add_to_cart()
    shop_page.in_cart()
    shop_page.click_checkout()
    shop_page.fill_form(
            first_name="Яша", last_name="Лорин",
            postal_code="123456")
    shop_page.checking_total_amount()
    driver.quit()
