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

     
