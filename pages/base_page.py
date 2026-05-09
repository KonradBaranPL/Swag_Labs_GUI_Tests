"""
Base page object model for all page objects.

Provides shared functionality and utilities available
to every page object inheriting from this class.
"""

from playwright.sync_api import Page

from utils.config import Config


class BasePage:
    """
    Base class for all page objects. 
    
    Uses an active Playwright `Page` instance
    to interact with the browser page.
    """

    def __init__(self, page: Page):
        self.page = page

    def get_current_url(self) -> str:
        """Return the current URL of the browser page."""
        return self.page.url

    def take_screenshot(self, filename: str):
        """Save a PNG screenshot to the configured screenshots directory."""
        self.page.screenshot(path=f"{Config.SCREENSHOTS_DIR}/{filename}.png")
