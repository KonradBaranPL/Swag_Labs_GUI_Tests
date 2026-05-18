"""module docstring"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """class docstring"""

    def __init__(self, page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.remove_buttons = page.locator("button[data-test^='remove']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
    

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        return self.item_names.all_text_contents()

    def remove_item_by_index(self, index: int):
        self.remove_buttons.nth(index).click()

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
