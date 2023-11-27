from selenium.webdriver.common.by import By
from random import randint


class FindSweaterLocators:
    SEARCH = (By.XPATH, "//input[contains(@placeholder, 'поиск')]/..")
    SEARCH2 = (By.XPATH, "//input[contains(@data-target, '_self')]")
    FIND = (By.XPATH, "//button[contains(text(), 'Найти')]")
    WOMEN = (By.XPATH, "//button[contains(text(), 'женский')]")
    STRIP = (By.XPATH, "//button[contains(text(), 'полоску')]")
    PRICE = (By.CSS_SELECTOR, "span[class='digi-product-price-variant digi-product-price-variant_actual']")


class RegistrateNewAccount:
    BUTTON = (By.CSS_SELECTOR, 'div[class="Profile__Button-sc-1ak7qq8-1 hbehmd"]')
    CREATE = (By.XPATH, '(//div[text()="создать"])')
    FIRST_NAME = (By.XPATH, '(//input[@name="firstName"])')
    LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    EMAIL = (By.XPATH, '//input[@name="email"]')
    PHONE = (By.XPATH, '//input[@name="phone"]')
    CHOOSE_GENDER = (By.XPATH, '//div[@style="margin-top: 1rem;"]')
    CHOOSE_GENDER2 = (By.XPATH, f'(//li[@class="FilledSelect__Option-sc-1mpv6q4-3 gBPSUf"])[{randint(2,3)}]')
    BIRTHDAY = (By.XPATH, '//div[@name="birthDate"]')
    BIRTHDAY_DAY = (By.XPATH, '//label[@for="birthDate"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    PASSWORD_ASSERT = (By.XPATH, '//input[@name="repeatPassword"]')
    AGREE = (By.XPATH, '//label[@for="checkbox"]')
    CREATE_NEW_ACC = (By.XPATH, '(//button[text()="создать аккаунт"])')
