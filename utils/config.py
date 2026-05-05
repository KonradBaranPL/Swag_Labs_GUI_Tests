import os


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    PRODUCTS_URL = os.getenv("PRODUCTS_URL", "https://www.saucedemo.com/inventory.html")
    CART_URL = os.getenv("CART_URL", "https://www.saucedemo.com/cart.html")

    FB_URL = os.getenv("FB_URL", "https://www.facebook.com/saucelabs")
    X_URL = os.getenv("X_URL", "https://x.com/saucelabs")
    LINKEDIN_URL = os.getenv("LINKEDIN_URL", "https://www.linkedin.com/company/sauce-labs/")

    DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT", "10000"))
    NAVIGATION_TIMEOUT = int(os.getenv("NAV_TIMEOUT", "30000"))
    SLOW_USER_TIMEOUT = 15000

    BROWSER = os.getenv("BROWSER", "chromium")

    SCREENSHOTS_DIR = "screenshots"
    REPORTS_DIR = "reports"
