"""
Page object model for the Swag Labs login page.

Provides locators for all interactive elements on the login page
and methods to navigate, perform login, and handle error messages.
"""

from pages.base_page import BasePage
from utils.config import Config
from playwright.sync_api import Page


class LoginPage(BasePage):
    """Page object representing the Swag Labs login page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test=\"error\"]")
        self.error_message_close_button = page.locator("[data-test=\"error-button\"]")
        self.logo = page.get_by_text("Swag Labs")

    def navigate(self):
        """Opens login page in the browser."""
        self.page.goto(Config.BASE_URL)

    def login(self, username, password):
        """Execute login with given username and password."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        """Returns text of error message displayed after failed login."""
        return self.error_message.text_content()

    def close_error(self):
        """Closes error message box."""
        self.error_message_close_button.click()
