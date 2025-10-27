from playwright.sync_api import expect
from pages.base_page import BasePage

BASKET = '[data-testid="basketTabIcon"]'
RESULT = '[class="_4e47b39f"]'
class LitresPage(BasePage):

    def open(self):
        self.page.goto('https://www.litres.ru/')

    def click_basket_my(self):
        basket = self.page.locator(BASKET)
        basket.click()

    def visible_words_my_text_is_(self, text):
        result = self.page.locator(RESULT)
        expect(result).to_have_text(text)
