from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import shutil
import requests
from utilities.reusableActions.Selenium_actions import SeleniumActions
from environment import get_browser_options
from utilities.reusableActions.Locust_actions import run_locust  # Import the run_locust function

@given('I have set up for load testing the login page')
def step_given_set_up_for_load_testing(context):
    if not shutil.which("locust"):
        raise RuntimeError("Locust is not installed. Please install Locust before running the tests.")

    # Start Locust
    context.process = run_locust(
        host='http://www.saucedemo.com',
        num_users=10,
        spawn_rate=1,
        web_port=9999
    )

    # Allow Locust to start up and the application to be accessible
    time.sleep(30)  # Adjust based on the startup time of Locust and the application

    # Check if the application is accessible
    url = "http://www.saucedemo.com"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError(f"The application is not accessible at {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to reach the application at {url}. Error: {e}")

@when('I perform login actions using Selenium')
def step_when_i_perform_login_actions_using_selenium(context):
    options = get_browser_options()

    # Manually specify the path to the chromedriver executable
    driver_path = r"C:\path\to\your\chromedriver.exe"  # Update this to your local chromedriver path
    print(f"Using ChromeDriver from: {driver_path}")

    # Initialize WebDriver
    context.driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=options)
    context.selenium_actions = SeleniumActions(context.driver)
    context.selenium_actions.navigate_to_url("https://www.saucedemo.com/")

    # Perform login actions
    context.selenium_actions.entertext_on_element("standard_user", (By.ID, "user-name"))
    context.selenium_actions.entertext_on_element("secret_sauce", (By.ID, "password"))
    context.selenium_actions.click_on_element((By.ID, "login-button"))

    # Verify successful login
    time.sleep(2)  # Wait for the page to load
    assert "inventory" in context.driver.current_url

@when('I simulate concurrent user logins')
def step_when_i_simulate_concurrent_user_logins(context):
    # Already handled by Locust
    pass

@then('the login page should handle the simulated load without issues')
def step_then_login_page_should_handle_load_without_issues(context):
    # Run the load test for a specific duration
    time.sleep(60)

    # Terminate the Locust process
    context.process.terminate()
    context.process.wait()

    # Capture and check output and errors
    stdout, stderr = context.process.communicate()
    if stderr:
        raise RuntimeError(f"Locust encountered an error: {stderr.decode('utf-8')}")

    if stdout:
        print(f"Locust output: {stdout.decode('utf-8')}")

    # Clean up Selenium WebDriver
    context.driver.quit()
