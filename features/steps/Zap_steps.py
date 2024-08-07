from behave import given, when, then
from selenium import webdriver
from utilities.reusableActions.Selenium_actions import SeleniumActions
from utilities.reusableActions.Zap_actions import ZapActions
from environment import get_browser_options
import time

@given('I am on the SwagLabs login page for security assessment')
def step_given_i_am_on_swaglabs_login_page_for_security(context):
    browser_options = get_browser_options()
    browser_options.add_argument("--proxy-server=http://localhost:8080")
    context.driver = webdriver.Chrome(options=browser_options)
    context.selenium_actions = SeleniumActions(context.driver)
    context.selenium_actions.navigate_to_url("https://www.saucedemo.com/")
    
    context.zap_actions = ZapActions()
    context.scan_id = context.zap_actions.start_scan("https://www.saucedemo.com/")

@when('I execute a security scan with ZAP')
def step_when_i_execute_security_scan_with_zap(context):
    try:
        while True:
            status = int(context.zap_actions.get_scan_status(context.scan_id))
            print(f"Current scan status: {status}%")

            if status % 10 == 0:
                print(f"Scan progress: {status}%")

            if status == 100:
                print("Scan complete.")
                break
            elif status < 0:
                print("Invalid scan status.")
                break

            time.sleep(10) 

    except Exception as e:
        print(f"Error executing scan: {e}")
        raise

@then('I should not discover any critical security vulnerabilities')
def step_then_i_should_not_discover_any_critical_security_vulnerabilities(context):
    try:
        alerts = context.zap_actions.get_scan_results("https://www.saucedemo.com/")
        print(f"Total alerts found: {len(alerts)}")
        for alert in alerts:
            print(f"Alert: {alert['alert']}")
            print(f"Description: {alert['description']}")
            print(f"Risk: {alert['risk']}")
            print(f"Message: {alert['message']}")
            print("\n")

        assert not any(alert['risk'] == 'High' for alert in alerts), "Critical security vulnerabilities found"

    except Exception as e:
        print(f"Error in verification step: {e}")
        raise
    finally:
        context.driver.quit()
