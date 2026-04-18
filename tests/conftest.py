"""fixtures"""

from pages.login_page import LoginPage
from playwright.sync_api import Page

import pytest


@pytest.fixture
def login_page(page: Page):
    """Returns an instance of LoginPage class"""
    return LoginPage(page)