from utilities.reusableActions.Selenium_actions import SeleniumActions

class SwagLabsLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)

    def open(self):
        self.actions.navigate_to_url("https://www.saucedemo.com/")

    def login(self, username, password):
        self.actions.entertext_on_element(username, ("id", "user-name"))
        self.actions.entertext_on_element(password, ("id", "password"))
        self.actions.click_on_element(("id", "login-button"))

    def click_login_button(self):
        self.actions.click_on_element(("id", "login-button"))
