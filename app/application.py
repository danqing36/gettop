from pages.main_page import MainPage
from pages.header import Header
from pages.product_list import ProductList

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.product_list = ProductList(self.driver)


