from playwright.sync_api import Page, expect
from pages.litres_page import LitresPage


def test_visible_lit(page: Page):
    litres_test = LitresPage(page)
    litres_test.open()
    litres_test.click_basket_my()
    litres_test.visible_words_my_text_is_('Корзина пуста')
