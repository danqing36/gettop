from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    CATEGORY_NAME = (By.XPATH, "//li[contains(@id,'menu-item')]/a[contains(@href,'{CATEGORY}')]")
    NEXT_PAGE=(By.XPATH, 'a.next.page-number')

    def _get_expected_category_locator(self, expected_category):
        return [self.CATEGORY_NAME[0], self.CATEGORY_NAME[1].replace('{CATEGORY}', expected_category)]

    def click_category(self, category_name: str):
        sleep(4)
        locator = self._get_expected_category_locator(category_name)
        self.click(*locator)

    def open_product_sort_page(self, order_by):
        self.open_page(order_by)


    def click_next_page(self):
        self.click(*self.NEXT_PAGE)
