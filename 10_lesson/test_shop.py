
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.shop_page import ShopPage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
import allure


@allure.title("Автотест на интернет-магазин")
@allure.description("Авторизация в интернет-магазине, добавление товаров в \
                     корзину, оформление заказа и проверка итоговой суммы.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)

def test_shop_page():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(
        ).install()))

    shop_page = ShopPage(driver)
    shop_page.open()
    login_page = LoginPage(driver)
    login_page.authorization()
    main_page = MainPage(driver)
    main_page.add_to_cart()
    cart_page = CartPage(driver)
    cart_page.in_cart()
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form(first_name="Иван", last_name="Петров",
            postal_code="123456")
    checkout_page.checking_total_amount()
    driver.quit()
