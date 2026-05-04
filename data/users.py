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
        return User(
            "standard_user",
            "secret_sauce",
            "website works properly",
        )
    
    @staticmethod
    def locked_out_user() -> User:
        return User(
            "locked_out_user",
            "secret_sauce",
            "blocked user, cannot log in",
        )
    
    @staticmethod
    def problem_user() -> User:
        return User(
            "problem_user",
            "secret_sauce",
            "website has several defects",
        )
    
    @staticmethod
    def performance_glitch_user() -> User:
        return User(
            "performance_glitch_user", 
            "secret_sauce", 
            "website simulates slow connection",
        )
    
    @staticmethod
    def error_user() -> User:
        return User(
            "error_user",
            "secret_sauce",
            "API returns code 500 errors",
        )
    
    @staticmethod
    def visual_user() -> User:
        return User(
            "visual_user",
            "secret_sauce",
            "website contains visual glitches",
        )