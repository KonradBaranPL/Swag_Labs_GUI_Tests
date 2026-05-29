"""
Tests for product sorting functionality on the Swag Labs inventory page.

Covers sorting products by name (A-Z, Z-A) and by price (ascending, descending).
"""

from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


class TestSorting:
    """Tests for the product sort dropdown on the inventory page."""

    def test_sorting_names_by_az(self, logged_in_page: Page):
        """Verifies that sorting by 'az' gives correct order"""
        # Arrange
        inventory = InventoryPage(logged_in_page)
        inventory.sort_by("za")

        # Act
        inventory.sort_by("az")
        names = inventory.get_all_product_names()

        # Assert
        assert names == sorted(names)

    def test_sorting_names_by_za(self, logged_in_page: Page):
        """Verifies that sorting by 'za' gives correct order"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.sort_by("za")
        names = inventory.get_all_product_names()

        # Assert
        assert names == sorted(names, reverse=True)

    def test_sorting_prices_ascending(self, logged_in_page: Page):
        """Verifies that sorting prices from lowest to highest gives correct order"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.sort_by("lohi")
        prices = inventory.get_all_prices()

        # Assert
        assert prices == sorted(prices)

    def test_sorting_prices_descending(self, logged_in_page: Page):
        """Verifies that sorting prices from highest to lowest gives correct order"""
        # Arrange
        inventory = InventoryPage(logged_in_page)

        # Act
        inventory.sort_by("hilo")
        prices = inventory.get_all_prices()

        # Assert
        assert prices == sorted(prices, reverse=True)
