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

    def get_items_count(self) -> int:
        """Returns the number of items currently in the cart."""
        return self.cart_items.count()

    def get_items_names(self) -> list[str]:
        """Returns a list of all item names currently in the cart."""
        return self.item_names.all_text_contents()

    def remove_item_by_index(self, index: int):
        """Removes an item from the cart by its position index."""
        self.remove_buttons.nth(index).click()

    def proceed_to_checkout(self):
        """Navigates to the checkout page."""
        self.checkout_button.click()

    def continue_shopping(self):
        """Navigates back to the inventory page."""
        self.continue_shopping_button.click()
