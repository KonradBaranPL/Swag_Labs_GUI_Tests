"""
Page object model for the Swag Labs checkout step two page.

Provides locators for order summary labels and methods
to read pricing details and complete the checkout process.
"""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """Page object representing the order summary step of the Swag Labs checkout process."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.subtotal_label = page.locator("[data-test=\"subtotal-label\"]")
        self.tax_label = page.locator("[data-test=\"tax-label\"]")
        self.total_label = page.locator("[data-test=\"total-label\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")

    def get_subtotal(self) -> float:
        """Returns the subtotal value as a float, with currency symbol stripped."""
        expect(self.subtotal_label).to_contain_text("$")
        return float(self.subtotal_label.text_content().split("$")[1])

    def get_tax(self) -> float:
        """Returns the tax value as a float, with currency symbol stripped."""
        expect(self.tax_label).to_contain_text("$")
        return float(self.tax_label.text_content().split("$")[1])

    def get_total(self) -> float:
        """Returns the total value as a float, with currency symbol stripped."""
        expect(self.total_label).to_contain_text("$")
        return float(self.total_label.text_content().split("$")[1])

    def finish(self):
        """Clicks the finish button to complete the order."""
        self.finish_button.click()
