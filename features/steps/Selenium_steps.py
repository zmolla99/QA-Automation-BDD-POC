from behave import given, when, then
from selenium.webdriver.common.by import By
from utilities.reusableActions.Selenium_actions import SeleniumActions
from environment import get_browser_options
from selenium import webdriver

@given('I am ready to log into SwagLabs')
def step_given_ready_to_log_into_swaglabs(context):
    options = get_browser_options()

    context.driver = webdriver.Chrome(options=options)
    context.selenium_actions = SeleniumActions(context.driver)
    context.selenium_actions.navigate_to_url("https://www.saucedemo.com/")

@when('I log in with valid credentials')
def step_when_i_log_in_with_valid_credentials(context):
    context.selenium_actions.entertext_on_element("standard_user", (By.ID, "user-name"))
    context.selenium_actions.entertext_on_element("secret_sauce", (By.ID, "password"))
    context.selenium_actions.click_on_element((By.ID, "login-button"))

@then('I should see the products page')
def step_then_i_should_see_the_products_page(context):
    context.selenium_actions.verify_title("Swag Labs")
    context.driver.quit() 