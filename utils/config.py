import os


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")

    DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT", "10000"))
    NAVIGATION_TIMEOUT = int(os.getenv("NAV_TIMEOUT", "30000"))
    SLOW_USER_TIMEOUT = 15000

    BROWSER = os.getenv("BROWSER", "chromium")

    SCREENSHOTS_DIR = "screenshots"
    REPORTS_DIR = "reports"
