"""
Tests for add-to-cart and remove-from-cart functionality on the Swag Labs inventory page.

Covers: cart badge updates, E2E product verification in cart,
button state change, removing from cart, and cart state persistence.
"""

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.config import Config


class TestAddToCart:
    """Tests for adding products to the cart from the inventory page."""

    def test_cart_bagde_updates_after_adding_one_product(self, logged_in_page: Page):
        """Verifies that after adding one product, cart badge shows number 1"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.add_product_by_name("Sauce Labs Backpack")

        # Assert
        expect(inventory.cart_badge).to_have_text("1")

    def test_add_three_products_to_cart(self, logged_in_page: Page):
        """Verifies that after adding three products, cart badge shows number 3"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.add_product_by_name("Sauce Labs Backpack")
        inventory.add_product_by_name("Sauce Labs Bike Light")
        inventory.add_product_by_name("Sauce Labs Bolt T-Shirt")

        # Assert
        expect(inventory.cart_badge).to_have_text("3")

    def test_added_product_is_in_the_cart(self, logged_in_page: Page):
        """Verifies that the selected product actually appears in the cart."""
        # Arrange
        inventory = InventoryPage(logged_in_page)
        expected_name = "Sauce Labs Backpack"

        # Act
        inventory.add_product_by_name(expected_name)
        inventory.go_to_cart()
        cart = CartPage(logged_in_page)

        # Assert
        expect(cart.page).to_have_url(Config.CART_URL)
        expect(cart.cart_items).to_have_count(1)
        expect(cart.cart_items.first).to_contain_text(expected_name)

    def test_add_button_changes_to_remove_after_adding(self, logged_in_page: Page):
        """Verifies that one product row changes from Add to cart to Remove"""
        # Arrange
        inventory = InventoryPage(logged_in_page)
        first_item = inventory.inventory_items.first
        add_button = first_item.locator("button[data-test^='add-to-cart']")
        remove_button = first_item.locator("button[data-test^='remove']")
        expect(add_button).to_be_visible()

        # Act
        add_button.click()

        # Assert
        expect(remove_button).to_be_visible()
        expect(add_button).to_be_hidden()


class TestRemoveFromCart:
    """Tests for removing products from the cart."""

    def test_remove_product_from_cart(self, logged_in_page: Page):
        """Verifies that an added product can be removed directly from the cart."""
        # Arrange
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()
        cart = CartPage(inventory.page)
        expect(cart.cart_items).to_have_count(1)

        # Act
        cart.remove_item_by_index(0)

        # Assert
        expect(cart.cart_items).to_have_count(0)
        expect(cart.cart_badge).to_be_hidden()

    def test_cart_remembers_product_after_returning_to_inventory(self, logged_in_page: Page):
        """Verifies that cart retains products after navigating back to the inventory."""
        # Arrange
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_by_name("Sauce Labs Backpack")
        inventory.add_product_by_name("Sauce Labs Bike Light")

        # Act
        inventory.go_to_cart()
        cart = CartPage(logged_in_page)
        cart.continue_shopping()

        # Assert
        expect(inventory.cart_badge).to_have_text("2")
