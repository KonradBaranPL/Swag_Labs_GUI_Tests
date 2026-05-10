# Swag Labs UI Test Automation Framework

## Project Overview

This project is a UI test automation framework built with Python, Pytest, and Playwright.

The framework automates end-to-end tests for the demo e-commerce application:

* [https://www.saucedemo.com/](https://www.saucedemo.com/)

The main goal of the project is to learn professional test automation practices and build a maintainable automation framework using modern tools and design patterns.

---

## Tech Stack

* Python
* Pytest
* Playwright
* pytest-playwright
* Page Object Model (POM)
* Git & GitHub

---

## Features

* UI and end-to-end testing
* Positive and negative test scenarios
* Page Object Model architecture
* Reusable fixtures and test data
* Configurable environment settings
* Screenshot capturing on test failure
* Smoke and regression test structure

---

## Project Structure

```text
swag-labs-tests/
│
├── tests/
├── pages/
├── data/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/swag-labs-tests.git
```

Create virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run tests in headed mode:

```bash
pytest --headed
```

Run smoke tests:

```bash
pytest -m smoke
```

---

## Project Goals

This project was created to practice:

* Playwright with Python,
* UI automation,
* scalable test architecture,
* clean and maintainable test code,
* real-world QA automation practices.

---

## Project Status

Project is currently under active development.

Planned improvements:

* CI/CD integration,
* API testing,
* reporting tools,
* parallel execution.

---

## License

This project is created for educational and portfolio purposes.
