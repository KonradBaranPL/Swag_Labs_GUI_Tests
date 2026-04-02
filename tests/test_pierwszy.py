"""missing docstring"""

from playwright.sync_api import Page, expect


def test_login_page_is_loading(page: Page):
    """Verifies that login page is loading and has correct tittle"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

# $ pytest tests\test_pierwszy.py --headed