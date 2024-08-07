from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class SeleniumActions:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def verify_title(self, page_title):
        assert self.driver.title == page_title, f"Expected: {page_title}, Actual: {self.driver.title}"

    def click_on_element(self, element_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element_locator)).click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element_locator))

    def entertext_on_element(self, text_to_enter, element_locator):
        self.driver.find_element(*element_locator).send_keys(text_to_enter)

    def generate_random_string(self, length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def generate_random_number(self, length):
        return ''.join(random.choice(string.digits) for _ in range(length))
