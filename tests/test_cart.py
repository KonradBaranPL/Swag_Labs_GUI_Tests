""" module docstring"""

from playwright.sync_api import Page, expect
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import Config


class TestAddToCart:
    """ class docstring """

    def test_add_one_product_to_cart(self, logged_in_page: Page):
        """Verifies that after adding one product, cart badge shows number 1"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.add_product_by_index(0)

        # Assert
        assert inventory.get_cart_count == 1

    def test_add_three_products_to_cart(self, logged_in_page: Page):
        """Verifies that after adding three products, cart badge shows number 3"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.add_product_by_index(0)
        inventory.add_product_by_index(1)
        inventory.add_product_by_index(2)

        # Assert
        assert inventory.get_cart_count == 3
    
    def test_added_product_is_in_the_cart(self, logged_in_page: Page):
        """Verifies that added product is in the cart after going to the cart page"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.add_product_by_index(0)
        inventory.go_to_cart()
        cart = CartPage(inventory.page)

        # Assert
        expect(cart.page).to_have_url(Config.CART_URL)
        products_in_cart = cart.cart_items
        expect(products_in_cart).to_have_count(1)



    def test_add_button_has_changed_to_remove_button(logged_in_page: Page):
        """Verifies that after clicking 'add' button, the button changed to 'remove' button"""
        # Arrange
        inventory = InventoryPage(logged_in_page)
        expect(inventory.add_buttons.first).to_be_visible()

        # Act
        inventory.add_product_by_index(0)

        # Assert
        expect(inventory.remove_buttons.first).to_be_visible()


class TestRemoveFromCart:
    """ class docstring"""

    def test_remove_product_from_cart(self, logged_in_page: Page):
        "Verifies that added product can be removed from cart"
        # Arrange 
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_by_index(0)
        inventory.go_to_cart()
        cart = CartPage(logged_in_page)
        assert cart.get_items_count() == 1

        # Act 
        cart.remove_item_by_index(0)

        # Assert
        assert cart.get_items_count() == 0

    def test_cart_remembered_added_products(self, logged_in_page: Page):
        """Verifies that cart remembers added products after going back
        from cart page to inventory page
        """
        # Arrange
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_by_index(0)
        inventory.add_product_by_index(1)

        # Act
        inventory.go_to_cart()
        CartPage(logged_in_page).continue_shopping()

        # Assert
        assert InventoryPage(logged_in_page).get_cart_count() == 2