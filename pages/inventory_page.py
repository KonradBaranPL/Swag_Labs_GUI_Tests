"""
Page object model for the Swag Labs inventory (products) page.

Provides locators for product listings, cart, sorting, footer social links,
and navigation menu, along with methods for reading page state and
performing user interactions.
"""
import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger("pages.inventory_page")


class InventoryPage(BasePage):
    """Page object representing the Swag Labs inventory (products) page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.get_by_test_id("title")
        self.inventory_items = page.get_by_test_id("inventory-item")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")
        self.cart_link = page.get_by_test_id("shopping-cart-link")
        self.product_sort_dropdown = page.get_by_test_id("product-sort-container")
        self.item_names = page.get_by_test_id("inventory-item-name")
        self.item_prices = page.get_by_test_id("inventory-item-price")

        self.add_buttons = page.get_by_test_id(re.compile(r"^add-to-cart"))
        self.remove_buttons = page.get_by_test_id(re.compile(r"^remove"))
        self.burger_menu = page.get_by_role("button", name="Open Menu")
        self.footer_x_button = page.get_by_test_id("social-twitter")
        self.footer_fb_button = page.get_by_test_id("social-facebook")
        self.footer_linkedin_button = page.get_by_test_id("social-linkedin")

    def get_all_product_names(self) -> list[str]:
        """Returns a list of all product names displayed on the inventory page."""
        expect(self.item_names).to_have_count(6)
        return self.item_names.all_text_contents()

    def get_all_prices(self) -> list[float]:
        """Returns a list of all product prices, with currency symbol stripped."""
        expect(self.item_names).to_have_count(6)
        texts = self.item_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in texts]

    def add_product_by_index(self, index: int):
        """Adds a product to the cart by its position index on the page."""
        logger.info("Adding product to cart at index: %d", index)
        self.add_buttons.nth(index).click()

    def add_product_by_name(self, product_name: str):
        """Adds a product to the cart by its name."""
        logger.info("Adding product to cart: %s", product_name)
        product = product_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test=\"add-to-cart-{product}\"]").click()

    def sort_by(self, value: str):
        """Sorts products using the dropdown menu.
        
        Args:
            value (str): Sort option — 'az', 'za', 'lohi', or 'hilo'.
        """
        logger.info("Sorting products by '%s'", value)
        self.product_sort_dropdown.select_option(value)

    def go_to_cart(self):
        """Navigates to the shopping cart page."""
        logger.info("Navigating to the cart")
        self.cart_link.click()

    def open_menu(self):
        """Opens the burger navigation menu."""
        logger.info("Opening navigation menu")
        self.burger_menu.click()
