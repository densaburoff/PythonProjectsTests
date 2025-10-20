from playwright.sync_api import Page, expect
from pages.my_first_page import MyFirstPage


def test_simple(page: Page):
    my_first_test = MyFirstPage(page)
    my_first_test.open()
    my_first_test.check_button_exist()
    my_first_test.click_button()
    my_first_test.check_result_text_is_('Submitted')