"""missing docstring"""

from playwright.sync_api import Page
from utils.config import Config
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def navigate(self):
        """Opens login page in the browser"""
        self.page.goto(Config.BASE_URL)