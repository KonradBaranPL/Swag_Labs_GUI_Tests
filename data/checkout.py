"""
Checkout data models and factory for the Swag Labs test suite.
"""

from dataclasses import dataclass


@dataclass
class CheckoutInfo:
    """Checkout form data with delivery address details"""
    first_name: str
    last_name: str
    postal_code: str


class  CheckoutFactory:
    """Factory class for creating predefined checkout data sets"""

    @staticmethod
    def valid() -> CheckoutInfo:
        """Returns a complete checkout data set with all fields filled in."""
        return CheckoutInfo(
            first_name="John",
            last_name="Doe",
            postal_code="12345",
        )

    @staticmethod
    def missing_first_name() -> CheckoutInfo:
        """Returns a checkout data set with an empty first name field."""
        return CheckoutInfo(
            first_name="",
            last_name="Doe",
            postal_code="12345",
        )

    @staticmethod
    def missing_last_name() -> CheckoutInfo:
        """Returns a checkout data set with an empty last name field."""
        return CheckoutInfo(
            first_name="John",
            last_name="",
            postal_code="12345",
        )

    @staticmethod
    def missing_postal_code() -> CheckoutInfo:
        """Returns a checkout data set with an empty postal code field."""
        return CheckoutInfo(
            first_name="John",
            last_name="Doe",
            postal_code="",
        )
