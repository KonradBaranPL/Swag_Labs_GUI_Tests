"""fixtures"""

import pytest
import logging
from playwright.sync_api import Page
from pages.login_page import LoginPage
from data.users import UserFactory
from utils.config import Config


# --- CONFIGURATION FIXTURES---
@pytest.fixture(autouse=True)
def setup_page(page: Page):
    """Sets automaticaly timeouts for each test"""
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    yield page

# --- DATA FIXTURES ---
@pytest.fixture
def standard_user():
    """Returns an instance of User class - standard_user"""
    return UserFactory.standard_user()

@pytest.fixture
def locked_out_user():
    """Returns an instance of User class - locked_out_user"""
    return UserFactory.locked_out_user()

@pytest.fixture
def problem_user():
    """Returns an instance of User class - problem_user"""
    return UserFactory.problem_user()

# --- PAGES FIXTURES ---
@pytest.fixture
def login_page(page: Page):
    """Returns an instance of LoginPage class"""
    return LoginPage(page)

@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """returns a page with standard_user already logged in"""
    user = UserFactory.standard_user()
    lp = LoginPage(page)
    lp.navigate()
    lp.login(user.username, user.password)
    return page

@pytest.fixture
def auth_page(page: Page, login_page) -> Page:
    user = UserFactory.standard_user()
    login_page.navigate()
    login_page.login(user.username, user.password)
    return page



# --- LOGGER ---
# logger = logging.getLogger("swag_labs_tests")
# --- SCREENSHOT ON FAILURE ---