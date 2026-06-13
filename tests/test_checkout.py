"""Tests for the Swag Labs checkout flow."""

import pytest
from playwright.sync_api import Page, expect

from data.checkout import CheckoutFactory
from pages.cart_page import CartPage
from pages.checkout_complete import CheckoutCompletePage
from pages.checkout_step_one import CheckoutStepOnePage
from pages.checkout_step_two import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from utils.config import Config


@pytest.mark.smoke
@pytest.mark.e2e
def test_complete_checkout_flow_for_logged_in_user(logged_in_page: Page):
    """Verifies full checkout flow for an already logged-in standard user."""
    # Arrange
    info = CheckoutFactory.valid()
    inventory = InventoryPage(logged_in_page)

    # Act
    inventory.go_to_cart()
    CartPage(logged_in_page).proceed_to_checkout()
    step_one = CheckoutStepOnePage(logged_in_page)
    step_one.fill_form(info.first_name, info.last_name, info.postal_code)
    step_one.continue_checkout()
    CheckoutStepTwoPage(logged_in_page).finish()

    # Assert
    complete = CheckoutCompletePage(logged_in_page)
    expect(complete.order_complete_header).to_have_text("Thank you for your order!")
    expect(logged_in_page).to_have_url(Config.CHECKOUT_COMPLETE_URL)

@pytest.mark.e2e
def test_order_summary_arithmetic_is_correct(at_checkout: Page):
    """Verifies that subtotal + tax equals the displayed total."""
    # Arrange
    info = CheckoutFactory.valid()
    step_one = CheckoutStepOnePage(at_checkout)
    step_one.fill_form(info.first_name, info.last_name, info.postal_code)
    step_one.continue_checkout()
    step_two = CheckoutStepTwoPage(at_checkout)

    # Act
    subtotal = step_two.get_subtotal()
    tax = step_two.get_tax()
    total = step_two.get_total()

    # Assert
    assert round(subtotal + tax, 2) == total, (
        f"Subtotal {subtotal} + tax {tax} = {round(subtotal + tax, 2)}, "
        f"expected {total}"
    )

@pytest.mark.negative
def test_checkout_fails_without_first_name(at_checkout: Page):
    """Verifies that checkout fails when the first name field is empty."""
    # Arrange
    info = CheckoutFactory.missing_first_name()
    step_one = CheckoutStepOnePage(at_checkout)

    # Act
    step_one.fill_form(info.first_name, info.last_name, info.postal_code)
    step_one.continue_checkout()

    # Assert
    expect(step_one.error_message).to_contain_text("First Name is required")

@pytest.mark.negative
def test_checkout_fails_without_last_name(at_checkout: Page):
    """Verifies that checkout fails when the last name field is empty."""
    # Arrange
    info = CheckoutFactory.missing_last_name()
    step_one = CheckoutStepOnePage(at_checkout)

    # Act
    step_one.fill_form(info.first_name, info.last_name, info.postal_code)
    step_one.continue_checkout()

    # Assert
    expect(step_one.error_message).to_contain_text("Last Name is required")

@pytest.mark.negative
def test_checkout_fails_without_postal_code(at_checkout: Page):
    """Verifies that checkout fails when the postal code field is empty."""
    # Arrange
    info = CheckoutFactory.missing_postal_code()
    step_one = CheckoutStepOnePage(at_checkout)

    # Act
    step_one.fill_form(info.first_name, info.last_name, info.postal_code)
    step_one.continue_checkout()

    # Assert
    expect(step_one.error_message).to_contain_text("Postal Code is required")
