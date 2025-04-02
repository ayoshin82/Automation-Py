

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open(self):
        self.driver.get(self.url)
