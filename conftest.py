import pytest
import os
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        # В CI/CD запускаем headless, локально - с браузером
        headless = os.getenv('CI') == 'true'
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()