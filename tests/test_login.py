"""
Test suite for the Swag Labs login page.

Covers:
- Page load and basic UI elements visibility
- Default state of input fields
- Successful login flow
- Negative login scenarios (invalid credentials, missing data, blocked user)

Uses Playwright with Page Object Model and predefined user fixtures.
"""

from playwright.sync_api import Page, expect

from data.users import User
from pages.login_page import LoginPage
from utils.config import Config


def test_login_page_has_loaded(page: Page, login_page: LoginPage):
    """Verifies that login page has loaded and has correct tittle"""
    # Act
    login_page.navigate()

    # Assert
    expect(page).to_have_url(Config.BASE_URL)
    expect(page).to_have_title("Swag Labs")


def test_swag_labs_logo_is_visible(login_page: LoginPage):
    """Verifies that "Swag Labs" logo is visible on the login page"""
    # Act
    login_page.navigate()

    # Assert
    expect(login_page.logo).to_be_visible()


def test_login_button_is_visible(login_page: LoginPage):
    """Verifies that login button is visible when login page has been loaded"""
    # Act
    login_page.navigate()

    # Assert
    expect(login_page.login_button).to_be_visible()


def test_username_field_is_empty(login_page: LoginPage):
    """Verifies that username field is empty when login page has been loaded"""
    # Act
    login_page.navigate()

    # Assert
    expect(login_page.username_input).to_have_value("")


def test_password_input_is_empty(login_page: LoginPage):
    """Verifies that password field is empty when login page has been loaded"""
    # Act
    login_page.navigate()

    # Assert
    expect(login_page.password_input).to_have_value("")


def test_successful_login(page: Page, login_page: LoginPage, standard_user: User):
    """Verifies that user logs in with valid credentials
    and is being redirected to product page
    """
    # Arrange
    login_page.navigate()

    # Act
    login_page.login(standard_user.username, standard_user.password)

    # Assert
    expect(page).to_have_url(Config.PRODUCTS_URL)


def test_login_with_blocked_user_fails(
        page: Page,
        login_page: LoginPage,
        locked_out_user: User,
):
    """Verifies that blocked user cannot log in and the page shows error message"""
    # Arrange
    login_page.navigate()

    # Act
    login_page.login(locked_out_user.username, locked_out_user.password)

    # Assert
    expect(page).to_have_url(Config.BASE_URL)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("this user has been locked out")


def test_login_without_username_fails(
        page: Page,
        login_page: LoginPage,
        standard_user: User,
):
    """Verifies that user cannot login if username field is empty"""
    # Arrange
    login_page.navigate()

    # Act
    login_page.password_input.fill(standard_user.password)
    login_page.login_button.click()

    # Assert
    expect(page).to_have_url(Config.BASE_URL)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username is required")


def test_login_without_password_fails(
        page: Page,
        login_page: LoginPage,
        standard_user: User,
):
    """Verifies that user cannot login if password field is empty"""
    # Arrange
    login_page.navigate()

    # Act
    login_page.username_input.fill(standard_user.username)
    login_page.login_button.click()

    # Assert
    expect(page).to_have_url(Config.BASE_URL)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Password is required")


def test_login_with_incorrect_username_fails(
        page: Page,
        login_page: LoginPage,
        standard_user: User,
):
    """Verifies that login with incorrect username fails"""
    # Arrange
    login_page.navigate()

    # Act
    login_page.username_input.fill("example_incorrect_user")
    login_page.password_input.fill(standard_user.password)
    login_page.login_button.click()

    # Assert
    expect(page).to_have_url(Config.BASE_URL)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )


def test_login_with_incorrect_password_fails(
        page: Page,
        login_page: LoginPage,
        standard_user: User,
):
    """Verifies that login with incorrect password fails"""
    # Arrange
    login_page.navigate()

    # Act
    login_page.username_input.fill(standard_user.username)
    login_page.password_input.fill("example_incorrect_password")
    login_page.login_button.click()

    # Assert
    expect(page).to_have_url(Config.BASE_URL)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )
