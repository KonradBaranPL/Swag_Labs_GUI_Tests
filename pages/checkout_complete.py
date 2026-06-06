"""Page object model for the Swag Labs checkout complete page."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page object representing the Swag Labs order confirmation page."""
    def __init__(self, page: Page):
        super().__init__(page)
        self.order_complete_header = page.get_by_test_id("complete-header")
        self.back_button = page.get_by_test_id("back-to-products")
