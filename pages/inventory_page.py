"""missing docstring"""

from pages.base_page import BasePage
from utils.config import Config
from playwright.sync_api import Page


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.locator("[data-test=\"title\"]")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")  # co to jest? nie znalazłem takiego lokatora
        self.cart_link = page.locator(".shopping_cart_link")  # dlaczego w ten sposób?
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")  # a nie w ten sposób?
        self.product_sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.add_buttons = page.locator("button[data-test^=\"add-to-cart\"]")
        self.remove_buttons = page.locator("button[data-test^=\"remove\"]")
        self.burger_menu = page.locator("#react-burger-menu-btn")  # dlaczego tak? co to za lokator?
        self.burger_menu_ver2 = page.get_by_role("button", name="Open Menu")  # dlaczego nie w ten sposób?
        # dodane przez mnie:
        self.footer_twitter_button = page.locator("[data-test=\"social-twitter\"]")
        self.footer_fb_button = page.locator("[data-test=\"social-facebook\"]")
        self.footer_linkedin_button = page.locator("[data-test=\"social-linkedin\"]")


 # metody odczytujące stan strony:
    def get_product_count(self) -> int:
        return self.inventory_items.count()
    
    def all_product_names(self) -> list[str]:
        return self.item_names.all_text_contents()
    
    def get_all_prices(self) -> list[float]:
        texts = self.item_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in texts]

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())

# metody wykonujące akcje
    def add_product_by_index(self, index: int):
        self.add_buttons.nth(index).click()

    def add_product_by_name(self, product_name: str):
        product = product_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test=\"add-to-cart-{product}\"]")

    def sort_by(self, value: str):
        """Possible values: 'az'. 'za', 'lohi, 'hilo"""
        self.product_sort_dropdown.select_option(value)

    def go_to_cart(self):
        self.cart_link.click()

    def open_menu(self):
        self.burger_menu.click()