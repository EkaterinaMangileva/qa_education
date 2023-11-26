from selenium.webdriver.common.by import By


class FindSweaterLocators:
    SEARCH = (By.XPATH, "//input[contains(@placeholder, 'поиск')]/..")
    SEARCH2 = (By.XPATH, "//input[contains(@data-target, '_self')]")
    FIND = (By.XPATH, "//button[contains(text(), 'Найти')]")
    WOMEN = (By.XPATH, "//button[contains(text(), 'женский')]")
    STRIP = (By.XPATH, "//button[contains(text(), 'полоску')]")
    PRICE = (By.CSS_SELECTOR, "span[class='digi-product-price-variant digi-product-price-variant_actual']")

