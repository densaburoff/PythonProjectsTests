from playwright.sync_api import Page
from pages.my_three_page import MyThreePage


def test_bingo(page: Page):
    my_three_test = MyThreePage(page)
    my_three_test.open()
    my_three_test.click_checkbox()
    my_three_test.click_button_three()

    my_three_test.expect_result_text_is_("select me or not")
