"""
Page object model for the Swag Labs inventory (products) page.

Provides locators for product listings, cart, sorting, footer social links,
and navigation menu, along with methods for reading page state and
performing user interactions.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object representing the Swag Labs inventory (products) page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.locator("[data-test=\"title\"]")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.product_sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.add_buttons = page.locator("button[data-test^=\"add-to-cart\"]")
        self.remove_buttons = page.locator("button[data-test^=\"remove\"]")
        self.burger_menu = page.get_by_role("button", name="Open Menu")
        self.footer_x_button = page.locator("[data-test=\"social-twitter\"]")
        self.footer_fb_button = page.locator("[data-test=\"social-facebook\"]")
        self.footer_linkedin_button = page.locator("[data-test=\"social-linkedin\"]")

    def get_product_count(self) -> int:
        """Returns the number of products displayed on the inventory page."""
        return self.inventory_items.count()

    def all_product_names(self) -> list[str]:
        """Returns a list of all product names displayed on the inventory page."""
        return self.item_names.all_text_contents()

    def get_all_prices(self) -> list[float]:
        """Returns a list of all product prices, with currency symbol stripped."""
        texts = self.item_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in texts]

    def get_cart_count(self) -> int:
        """Returns the number of items in the cart, or 0 if the cart badge is not visible."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def add_product_by_index(self, index: int):
        """Adds a product to the cart by its position index on the page."""
        self.add_buttons.nth(index).click()

    def add_product_by_name(self, product_name: str):
        """Adds a product to the cart by its name."""
        product = product_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test=\"add-to-cart-{product}\"]").click()

    def sort_by(self, value: str):
        """Sorts products using the dropdown menu.
        
        Args:
            value (str): Sort option — 'az', 'za', 'lohi', or 'hilo'.
        """
        self.product_sort_dropdown.select_option(value)

    def go_to_cart(self):
        """Navigates to the shopping cart page."""
        self.cart_link.click()

    def open_menu(self):
        """Opens the burger navigation menu."""
        self.burger_menu.click()
