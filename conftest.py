import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import pytest_html


@pytest.fixture
def config():
    with open("config.json") as f:
        return json.load(f)


@pytest.fixture
def driver(config):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(config["url"])

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":
        driver = item.funcargs.get("driver")

        if report.failed and driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_name)

            extra.append(pytest_html.extras.image(screenshot_name))

    report.extra = extra