"""missing docstring"""

from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"


def test_successful_login(page):
    """Verifies that user logs in with valid credentials
    and is being redirected to product page
    """
    # Arrange - open login page
    page.goto(URL)

    # Act - fill the login form and click login button
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert - verify that user is logged in and is navigated to the product page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_have_text("Products")


def test_products_are_visible_after_login(page):
    """docstring"""
    # Arrange - open login page
    page.goto(URL)

    # Act - fill the login form and click login button
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert - verify that user is logged in and is navigated to the product page
    products = page.locator(".inventory_item")
    expect(products).to_have_count(6)


def test_login_fails_with_blocked_user(page):
    """Verifies that blocked user cannot log in
    and the page shows error message"""

    # Arrange - open login page
    page.goto(URL)

    # Act - fill the login form and click login button
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert
    expect(page).to_have_url("https://www.saucedemo.com/")
    # expect(page.locator("[data-test=\"error\"]")) # co dalej?
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

# $ pytest tests\test_login.py -v --headed
