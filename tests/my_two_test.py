from playwright.sync_api import Page

from pages.my_two_page import MyTwoPage


def test_like(page: Page):
    my_two_test = MyTwoPage(page)
    my_two_test.open()
    my_two_test.check_button_visible()


def test_like_click(page: Page):
    my_two_test = MyTwoPage(page)
    my_two_test.open()
    my_two_test.click_the_button()
