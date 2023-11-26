import random
import time

from locators.elements_page_locators import FindSweaterLocators
from pages.base_page import BasePage


class FindSweaterPage(BasePage):
    locators = FindSweaterLocators()

    def find_xl_sweater_price(self):
        self.element_is_visible(FindSweaterLocators.SEARCH).click()
        self.element_is_visible(FindSweaterLocators.SEARCH2).send_keys('свитер')
        self.element_is_visible(self.locators.FIND).click()
        self.element_is_visible(self.locators.WOMEN).click()
        self.element_is_visible(self.locators.STRIP).click()
        prises = self.elements_are_present(self.locators.PRICE)
        return prises

    def check_filled_form(self):
        search = self.element_is_present(self.locators.SEARCH).text
