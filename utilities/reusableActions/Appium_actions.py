from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
import time

class AppiumActions:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_on_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        element.click()

    def entertext_on_element(self, text_to_enter, element_locator):
        element = self.driver.find_element(*element_locator)
        element.send_keys(text_to_enter)
