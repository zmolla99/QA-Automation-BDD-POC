from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

class AppiumLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(AppiumBy.ID, "user-name").send_keys(username)
        self.driver.find_element(AppiumBy.ID, "password").send_keys(password)
        self.driver.find_element(AppiumBy.ID, "login-button").click()
