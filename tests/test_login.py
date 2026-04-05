from pages.login_page import LoginPage
import json

def test_valid_login(driver):
    with open("config.json") as f:
        config=json.load(f)
    login_page = LoginPage(driver)

    login_page.login(config["username"], config["password"])

    assert login_page.get_title_text() == "Products"
