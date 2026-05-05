"""missing docstring"""

from playwright.sync_api import Page
from utils.config import Config



def test_products_are_visible_on_inventory_page(authenticated_page: Page):
    """docstring"""
    # Arrange - open login page
    inv_page = authenticated_page

    # Act - fill the login form and click login button
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Assert - verify that user is logged in and is navigated to the product page
    products = page.locator(".inventory_item")
    expect(products).to_have_count(6)

def test_inventory_page_has_correct_tittle(authenticated_page):
    """Verifies that products page has title 'Products'."""
    # Arrange
    inv_page = authenticated_page

    # Assert

    pass

def test_every_product_can_be_added_to_cart(authenticated_page):
    pass