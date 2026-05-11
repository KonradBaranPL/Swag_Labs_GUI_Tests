"""
Tests for the Swag Labs inventory (products) page.

Covers page title verification, product listing display,
and footer social media links redirecting to correct URLs.
"""

from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from utils.config import Config


def test_inventory_page_has_correct_title(authenticated_page: Page):
    """Verifies that products page has title 'Products'."""
    # Arrange
    inventory = InventoryPage(authenticated_page)

    # Assert
    expect(inventory.page_title).to_have_text("Products")


def test_products_are_visible_on_inventory_page(authenticated_page: Page):
    """Verifies that products page displays six products"""
    # Arrange
    inventory = InventoryPage(authenticated_page)

    # Assert
    products = inventory.inventory_items
    expect(products).to_have_count(6)


def test_facebook_button_redirects_to_correct_url(page: Page, authenticated_page: Page):
    """Verifies that facebook button redirects to Sauce Labs facebook profile"""
    # Arrange
    inventory = InventoryPage(authenticated_page)

    # Act
    with page.expect_popup() as page1_info:
        inventory.footer_fb_button.click()
    page1 = page1_info.value

    # Assert
    expect(page1).to_have_url(Config.FB_URL)


def test_x_button_redirects_to_correct_url(page: Page, authenticated_page: Page):
    """Verifies that x.com button redirects to Sauce Labs x.com profile"""
    # Arrange
    inventory = InventoryPage(authenticated_page)

    # Act
    with page.expect_popup() as page1_info:
        inventory.footer_x_button.click()
    page1 = page1_info.value

    # Assert
    expect(page1).to_have_url(Config.X_URL)


def test_linkedin_button_redirects_to_correct_url(page: Page, authenticated_page: Page):
    """Verifies that linkedin button redirects to Sauce Labs linkedin profile"""
    # Arrange
    inventory = InventoryPage(authenticated_page)

    # Act
    with page.expect_popup() as page1_info:
        inventory.footer_linkedin_button.click()
    page1 = page1_info.value

    # Assert
    expect(page1).to_have_url(Config.LINKEDIN_URL)
