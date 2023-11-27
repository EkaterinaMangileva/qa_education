from pages.elements_page import FindSweaterPage
from pages.elements_page import RegistrateNewAccountPage


class TestSweater:
    def test_sweater_price(self, driver):
        test_sweater = FindSweaterPage(driver, "https://befree.ru/")
        test_sweater.open()
        prices = test_sweater.find_xl_sweater_price()
        print(prices)
        lll = []
        for item in prices:
            lll.append(item.text)
            print(item.text)
        assert '4 599 ₽' in lll


class TestNewAccount:
    def test_new_account(self, driver):
        test_account = RegistrateNewAccountPage(driver, "https://befree.ru/")
        test_account.open()
        first_name, last_name, email, phone, birthday_day, password = test_account.create_new_account()
        first_name, last_name, email, phone, birthday_day, password = test_account.check_filled_form()
        print(test_account.check_filled_form())
