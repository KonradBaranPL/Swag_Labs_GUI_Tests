"""missing docstring"""

from playwright.sync_api import Page, expect


def test_login_page_is_loading(page: Page):
    """Verifies that login page is loading and has correct tittle"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")


def test_login_button_is_visible(page):
    """Verifies that login button is visible on login page"""
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()


def test_username_field_is_empty(page):
    """Verifies that username field is empty after login page has been loaded"""
    page.goto("https://www.saucedemo.com/")
    pass


def test_swag_labs_logo_is_visible():
    pass


# $ pytest tests\test_pierwszy.py --headed