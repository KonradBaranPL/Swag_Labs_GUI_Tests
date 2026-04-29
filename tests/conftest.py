"""fixtures"""

import pytest
import logging
from playwright.sync_api import Page
from pages.login_page import LoginPage
from data.users import UserFactory
from utils.config import Config


@pytest.fixture
def login_page(page: Page):
    """Returns an instance of LoginPage class"""
    return LoginPage(page)


# Logger
logger = logging.getLogger("swag_labs_tests")


# --- CONFIGURATION ---
@pytest.fixture(autouse=True)
def setup_page(page: Page):
    """Sets automaticaly timeouts for each test"""
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    yield page