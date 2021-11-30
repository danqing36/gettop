from pages.base_page import Page
from selenium.webdriver.common.by import By



class Header(Page):
    CATEGORY_NAME = (By.XPATH, "//li[contains(@id,'menu-item')]/a[contains(@href,'{CATEGORY}')]")

    def _get_expected_category_locator(self, expected_category):
        return [self.CATEGORY_NAME[0], self.CATEGORY_NAME[1].replace('{CATEGORY}', expected_category)]

    def click_category(self, category_name: str):
        locator = self._get_expected_category_locator(category_name)
        self.click(*locator)
