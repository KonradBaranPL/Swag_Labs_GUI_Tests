"""
Page object model for the Swag Labs checkout step one page.

Provides locators for the delivery information form and methods
to fill in the form and navigate through the checkout process.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Page object representing the first step of the Swag Labs checkout process."""
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.get_by_test_id("firstName")
        self.last_name_input = page.get_by_test_id("lastName")
        self.postal_code_input = page.get_by_test_id("postalCode")
        self.continue_button = page.get_by_test_id("continue")
        self.cancel_button = page.get_by_test_id("cancel")
        self.error_message = page.get_by_test_id("error")

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """Fills in the checkout form with the provided delivery information."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        """Submits the checkout form and proceeds to the next step."""
        self.continue_button.click()
