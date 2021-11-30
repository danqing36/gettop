from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductList(Page):
    SORT = (By.NAME, 'orderby')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.price')

    def select_sort(self, sort_method: str):
        select = Select(self.find_element(*self.SORT))
        select.select_by_visible_text(sort_method)


    def get_product_list(self, price_list):
        products = self.find_elements(*self.PRODUCT_PRICE)
        for price in products:
            if price.text.count('$')==1:
                price_list.append(int(price.text[1:].split('.')[0].replace(',','')))
            else:
                templist = price.text.split(' ')
                price_list.append(int(templist[1][1:].split('.')[0].replace(',','')))
        return price_list

