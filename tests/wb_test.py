import pytest
from playwright.sync_api import Page, expect


def test_wb(page: Page):
    # Увеличиваем таймауты
    page.set_default_timeout(15000)

    page.goto(
        'https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%82%D0%B5%D0%BB%D0%B5%D0%B2%D0%B8%D0%B7%D0%BE%D1%80')

    # Ожидаем загрузки
    page.wait_for_selector('.product-card', state='visible', timeout=20000)

    # Берем первую кнопку добавления в корзину
    add_button = page.locator('a.product-card__add-basket.j-add-to-basket').first

    # Проверяем что кнопка видима перед кликом
    expect(add_button).to_be_visible()

    # Кликаем
    add_button.click()

    # Ждем изменения текста
    try:
        expect(add_button).to_have_text("В корзине", timeout=15000)
        print("✅ Текст кнопки изменился на 'В корзине'")
    except:
        expect(add_button).to_contain_text("корзине", timeout=8000)
        print("✅ Текст кнопки содержит 'корзине'")

