"""
Page object model for the Swag Labs shopping cart page.

Provides locators for cart items, prices, and action buttons,
along with methods for reading cart state and performing user interactions.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """Represents the shopping cart page with item management and navigation."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.remove_buttons = page.locator("button[data-test^='remove']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def remove_item_by_index(self, index: int):
        """Removes an item from the cart by its position index."""
        self.remove_buttons.nth(index).click()

    def proceed_to_checkout(self):
        """Navigates to the checkout page."""
        self.checkout_button.click()

    def continue_shopping(self):
        """Navigates back to the inventory page."""
        self.continue_shopping_button.click()
