from behave import given, when, then
from selenium import webdriver
from utilities.reusableActions.Selenium_actions import SeleniumActions
from environment import get_browser_options
from axe_selenium_python import Axe

@given('I am on the SwagLabs login page for accessibility testing')
def step_given_i_am_on_swaglabs_login_page_for_accessibility(context):
    options = get_browser_options()  # This should return a `webdriver.ChromeOptions` object

    context.driver = webdriver.Chrome(options=options)
    context.selenium_actions = SeleniumActions(context.driver)
    context.selenium_actions.navigate_to_url("https://www.saucedemo.com/")
    context.axe = Axe(context.driver)

@when('I run an accessibility scan on the login page')
def step_when_i_run_accessibility_scan_on_login_page(context):
    context.axe.inject()
    context.results = context.axe.run()

@then('I should not find any accessibility issues')
def step_then_i_should_not_find_any_accessibility_issues(context):
    violations = context.results.get("violations", [])
    print(f"Accessibility violations found: {violations}")
    assert not violations, "Accessibility issues found"
    context.driver.quit()
