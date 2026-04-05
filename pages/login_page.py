from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils 

class LoginPage:

    def __init__(self, driver):
        self.wait = WaitUtils(driver)  

    # locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    title = (By.CLASS_NAME, "title")

    # actions
    def login(self, user, pwd):
        self.wait.wait_for_element(self.username).send_keys(user)
        self.wait.wait_for_element(self.password).send_keys(pwd)
        self.wait.wait_for_clickable(self.login_btn).click()
     
    def get_title_text(self):
        return self.wait.wait_for_element(self.title).text