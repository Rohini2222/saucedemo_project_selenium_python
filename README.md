# 🧪 Selenium Python Automation Framework (Pytest)

## 📌 Overview

This project is a Selenium-based automation framework built using **Python and Pytest**. It is designed with a focus on scalability, maintainability, and clean test architecture.

The framework follows the **Page Object Model (POM)** pattern and includes structured test layers, reusable utilities, logging, and reporting.

---

## 🚀 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* WebDriver Manager
* pytest-html (for reporting)

---

## 📁 Project Structure

```
saucedemo_project_selenium_python/
│
├── pages/              # Page Object classes (UI actions & locators)
├── tests/              # Test cases
├── utils/              # Utility functions (waits, helpers)
├── reports/            # HTML test reports
├── screenshots/        # Screenshots captured during execution
├── assets/             # Test data or static resources
├── conftest.py         # Pytest fixtures (setup & teardown)
├── pytest.ini          # Pytest configuration
```

---

## 🧠 Framework Highlights

* Page Object Model (POM) for better code organization
* Reusable utility methods for handling waits and common actions
* Pytest fixtures for driver management
* Integrated logging and HTML reporting
* Clean and readable test design

---

## ▶️ Setup & Execution

### 1. Clone the repository

```bash
git clone https://github.com/Rohini2222/saucedemo_project_selenium_python.git
cd saucedemo_project_selenium_python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Execute tests

```bash
pytest
```

---

## 📊 Reports

HTML reports are generated after execution in:

```
/reports/report.html
```

---

## 🔧 Notes

* The framework is designed to be easily extendable for additional test scenarios.
* Supports structured test development with separation of concerns.

---
