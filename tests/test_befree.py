from pages.elements_page import FindSweaterPage


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
