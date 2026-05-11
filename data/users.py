"""
User data models and factory for the Swag Labs test suite.

Provides a User dataclass and a UserFactory with static methods
for creating predefined test user accounts available in the application:

- standard_user:           website works properly
- locked_out_user:         blocked user, cannot log in
- problem_user:            website has several defects
- performance_glitch_user: website simulates slow connection
- error_user:              API returns code 500 errors
- visual_user:             website contains visual glitches
"""

from dataclasses import dataclass


@dataclass
class User:
    """Swag Labs test user with login credentials and behavior description."""
    username: str
    password: str
    description: str


class UserFactory:
    """Factory class for creating predefined Swag Labs test users with known behaviors."""

    @staticmethod
    def standard_user() -> User:
        """Returns a standard user — the website works properly for this account."""
        return User(
            "standard_user",
            "secret_sauce",
            "website works properly",
        )

    @staticmethod
    def locked_out_user() -> User:
        """Returns a locked-out user who cannot log in."""
        return User(
            "locked_out_user",
            "secret_sauce",
            "blocked user, cannot log in",
        )

    @staticmethod
    def problem_user() -> User:
        """Returns a problem user — the website has several defects on this account."""
        return User(
            "problem_user",
            "secret_sauce",
            "website has several defects",
        )

    @staticmethod
    def performance_glitch_user() -> User:
        """Returns a performance glitch user — the website simulates a slow connection on this account."""
        return User(
            "performance_glitch_user", 
            "secret_sauce", 
            "website simulates slow connection",
        )

    @staticmethod
    def error_user() -> User:
        """Returns an error user — the API returns code 500 errors on this account."""
        return User(
            "error_user",
            "secret_sauce",
            "API returns code 500 errors",
        )

    @staticmethod
    def visual_user() -> User:
        """Returns a visual user — the website contains visual glitches on this account."""
        return User(
            "visual_user",
            "secret_sauce",
            "website contains visual glitches",
        )
