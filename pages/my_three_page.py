from playwright.sync_api import expect
from pages.base_page import BasePage


CHECKBOX = '#id_checkbox_0'
BUTTON = '#submit-id-submit'
RESULT = "#result-text"
class MyThreePage(BasePage):

    def open(self):
        self.page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    def click_checkbox(self):
        checkbox = self.page.locator(CHECKBOX)
        checkbox.click()

    def click_button_three(self):
        button = self.page.locator(BUTTON)
        button.click()

    def expect_result_text_is_(self, text):
        result_text = self.page.locator(RESULT)
        expect(result_text).to_have_text(text)
