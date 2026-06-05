"""
Pytest fixtures for UI tests of the Swag Labs application.

Provides configuration, data, and page object fixtures
shared across all test modules via conftest.py.
"""

from playwright.sync_api import Page, Playwright
import pytest

from data.users import UserFactory
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import Config


# --- CONFIGURATION FIXTURES---
@pytest.fixture(scope="session", autouse=True)
def configure_playwright_locators(playwright: Playwright):
    """Configures Playwright to use 'data-test' as the default test ID attribute"""
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(autouse=True)
def setup_page(page: Page):
    """Sets automaticaly timeouts for each test"""
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    yield page


# --- DATA FIXTURES ---
@pytest.fixture
def standard_user():
    """Returns an instance of User class - standard_user."""
    return UserFactory.standard_user()

@pytest.fixture
def locked_out_user():
    """Returns an instance of User class - locked_out_user."""
    return UserFactory.locked_out_user()

@pytest.fixture
def problem_user():
    """Returns an instance of User class - problem_user."""
    return UserFactory.problem_user()


# --- PAGES FIXTURES ---
@pytest.fixture
def login_page(page: Page):
    """Returns an instance of LoginPage class."""
    return LoginPage(page)

@pytest.fixture
def logged_in_page(page: Page, login_page: LoginPage):
    """Returns a products page with standard_user already logged in."""
    user = UserFactory.standard_user()
    login_page.navigate()
    login_page.login(user.username, user.password)
    return page

@pytest.fixture
def at_checkout(logged_in_page: Page) -> Page:
    """Returns logged-in user with one product, positioned on checkout step one."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_product_by_index(0)
    inventory.go_to_cart()
    CartPage(logged_in_page).proceed_to_checkout()
    return logged_in_page
