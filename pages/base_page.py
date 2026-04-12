"""missing dockstring"""

from playwright.sync_api import Page
from utils.config import Config


class BasePage:

    def __init__(self, page: Page):
        self.page = page
    
    def get_current_url(self):
        return self.page.url

    def take_screenshot(self, filename):
        self.page.screenshot(path=f"{Config.SCREENSHOTS_DIR}/{filename}.png")