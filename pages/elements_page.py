import random
import time

from locators.elements_page_locators import FindSweaterLocators, RegistrateNewAccount
from pages.base_page import BasePage
from generator.generator import generated_person


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


class RegistrateNewAccountPage(BasePage):
    locators = RegistrateNewAccount()

    def create_new_account(self):
        person = next(generated_person())
        self.element_is_visible(RegistrateNewAccount.BUTTON).click()
        self.element_is_visible(RegistrateNewAccount.CREATE).click()
        self.element_is_visible(RegistrateNewAccount.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(RegistrateNewAccount.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(RegistrateNewAccount.EMAIL).send_keys(person.email)
        self.element_is_visible(RegistrateNewAccount.PHONE).send_keys(person.phone)
        self.element_is_visible(RegistrateNewAccount.CHOOSE_GENDER).click()
        self.element_is_visible(RegistrateNewAccount.CHOOSE_GENDER2).click()
        self.element_is_visible(RegistrateNewAccount.BIRTHDAY).click()
        self.element_is_visible(RegistrateNewAccount.BIRTHDAY_DAY).send_keys(person.birthday_day)
        self.element_is_visible(RegistrateNewAccount.PASSWORD, RegistrateNewAccount.PASSWORD_ASSERT).send_keys(person.password)
        self.element_is_visible(RegistrateNewAccount.AGREE).click()
        self.element_is_visible(RegistrateNewAccount.CREATE_NEW_ACC).click()

    def check_filled_form(self):
        first_name = self.element_is_present(RegistrateNewAccount.FIRST_NAME).text
        last_name = self.element_is_present(RegistrateNewAccount.LAST_NAME).text
        email = self.element_is_present(RegistrateNewAccount.EMAIL).text
        phone = self.element_is_present(RegistrateNewAccount.PHONE).text
        birthday_day = self.element_is_present(RegistrateNewAccount.BIRTHDAY_DAY).text
        password = self.element_is_present(RegistrateNewAccount.PASSWORD).text
        password2 = self.element_is_present(RegistrateNewAccount.PASSWORD_ASSERT).text
        return first_name, last_name, email, phone, birthday_day, password, password2
