# Swag Labs GUI Tests

## Table of Contents

- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started Locally](#getting-started-locally)
- [Running Tests](#running-tests)
- [Project Status](#project-status)

---

## Project Description

Project Description
An automated end-to-end UI test suite for Swag Labs — a demo e-commerce application built specifically for testing practice. 

The project is built around the Page Object Model pattern, separating locators and user interactions from test logic. Test data is managed through the Factory pattern, providing predefined user accounts with known behaviors. Shared state and setup are handled via pytest fixtures, keeping individual tests focused and independent. Environment-specific values such as URLs and timeouts are centralized in a dedicated configuration layer, making the suite easy to run across different environments.

---

## Tech Stack

- **Python** 3.8+
- **pytest** 8.4.2 – test framework
- **Playwright** 1.58.0 – browser automation
- **pytest-playwright** 0.7.2 – Playwright integration for pytest
- **pytest-html** 4.2.0 – HTML test reporting
- **pytest-cov** – test coverage reporting

---

## Getting Started Locally

**Clone the repository:**

```bash
git clone https://github.com/KonradBaranPL/Swag_Labs_GUI_Tests.git
cd Swag_Labs_GUI_Tests
```

**Create and activate a virtual environment:**

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Install Playwright browsers:**

```bash
playwright install
```

**Configure environment (optional):**

The base URL and timeouts default to production values. To override them, set environment variables before running tests:

```bash
# Linux/macOS
export BASE_URL=https://www.saucedemo.com/
export TIMEOUT=10000

# Windows
set BASE_URL=https://www.saucedemo.com/
```

---

## Running Tests

```bash
# Run all tests
pytest

# Run with visible browser
pytest --headed

# Run a specific test file
pytest tests/test_login.py
pytest tests/test_inventory_page.py

# Run with verbose output
pytest -v

# Generate an HTML report
pytest --html=report.html
```

---

## Project Status

### ✅ Done

- Page Object Model architecture with a shared `BasePage` class
- `LoginPage` with full locator coverage and login/error methods
- `InventoryPage` with locators for products, cart, sorting, footer links, and burger menu
- `User` dataclass and `UserFactory` covering all six Swag Labs user types (standard, locked out, problem, performance glitch, error, visual)
- `conftest.py` with shared fixtures: timeout setup, user fixtures, `login_page`, `authenticated_page`
- Login tests — page load checks, positive login flow, and negative scenarios (blocked user, missing username, missing password, incorrect credentials)
- Inventory tests — page title, product count, and footer social link redirects (Facebook, X, LinkedIn)
- Environment-based configuration via `utils/config.py`
- PEP 8 compliance, type annotations, and docstrings throughout

### 🔧 Planned

- `CartPage` implementation and cart tests (add/remove items, cart state persistence)
- Sorting tests — alphabetical and price-based, ascending and descending
- Checkout flow — Page Objects and E2E tests for the full purchase path
- Test coverage for additional user types (problem user, visual user behaviors)
- Parametrized tests across multiple user types
- Data-driven test scenarios
- Multi-browser execution (Firefox, WebKit)
- CI/CD integration via GitHub Actions