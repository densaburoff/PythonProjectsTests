from playwright.sync_api import expect
from pages.base_page import BasePage
BUTTON = '.a-button'


class MyTwoPage(BasePage):

    def open(self):
        self.page.goto('https://www.qa-practice.com/elements/button/like_a_button')

    def check_button_visible(self):
        button = self.page.locator(BUTTON)
        expect(button).to_be_visible()

    def click_the_button(self):
        button = self.page.locator(BUTTON)
        button.click()