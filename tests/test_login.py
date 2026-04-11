"""missing docstring"""

from playwright.sync_api import Page, expect

MAIN_PAGE_URL = "https://www.saucedemo.com/"


def test_successful_login(page):
    """Verifies that user logs in with valid credentials
    and is being redirected to product page
    """
    # Arrange - open login page
    page.goto(MAIN_PAGE_URL)

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
    page.goto(MAIN_PAGE_URL)

    # Act - fill the login form and click login button
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert - verify that user is logged in and is navigated to the product page
    products = page.locator(".inventory_item")
    expect(products).to_have_count(6)


def test_login_with_blocked_user_fails(page):
    """Verifies that blocked user cannot log in
    and the page shows error message"""

    # Arrange - open login page
    page.goto(MAIN_PAGE_URL)

    # Act - fill the login form and click login button
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert - verify that error message is shown and user is not redirected to another page
    expect(page).to_have_url("https://www.saucedemo.com/")
    error = page.locator("[data-test=\"error\"]")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Sorry, this user has been locked out.")


def test_login_without_username_fails(page):
    """Verifies that user cannot login if username field is empty
    and the page shows error message
    """

    # Arrange
    page.goto(MAIN_PAGE_URL)

    # Act
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert
    expect(page).to_have_url("https://www.saucedemo.com/")
    error = page.locator("[data-test=\"error\"]")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username is required")


def test_login_without_password_fails(page):
    """Verifies that user cannot login if password field is empty
    and the page shows error message
    """

    # Arrange
    page.goto(MAIN_PAGE_URL)

    # Act
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert
    expect(page).to_have_url("https://www.saucedemo.com/")
    error = page.locator("[data-test=\"error\"]")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Password is required")






# $ pytest tests\test_login.py -v --headed