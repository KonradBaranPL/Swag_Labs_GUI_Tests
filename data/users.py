from dataclasses import dataclass


@dataclass
class User:
    """test user data"""
    username: str
    password: str
    description: str


class UserFactory:

    @staticmethod
    def standard_user() -> User:
        return User("standard_user", "secret_sauce", "the website is working properly")
    