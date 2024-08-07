from behave import given, when, then
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from utilities.reusableActions.Appium_actions import AppiumActions
from environment import get_appium_config
from pages.login.appium_login import AppiumLoginPage  
from appium.options.android import UiAutomator2Options

@given('I have the SwagLabs mobile app open')
def step_given_i_have_swaglabs_app_open(context):
    appium_config = get_appium_config()
    
    options = UiAutomator2Options()
    options.platform_name = appium_config["platform_name"]
    options.device_name = appium_config["device_name"]
    options.browser_name = appium_config["browser_name"]
    
    print(f"Capabilities: {options.to_capabilities()}")
    print(f"Appium Server URL: {appium_config['appium_server_url']}")
    
    try:
        context.driver = webdriver.Remote(appium_config["appium_server_url"], options=options)
        context.appium_actions = AppiumActions(context.driver)
        context.login_page = AppiumLoginPage(context.driver) 
        
        context.driver.get("https://www.saucedemo.com/")
    except Exception as e:
        print(f"Error connecting to Appium server: {e}")
        raise

@when('I interact with the mobile app')
def step_when_i_interact_with_the_mobile_app(context):
    username = "standard_user"  
    password = "secret_sauce"   
    
    context.login_page.login(username, password)

@then('I should see the main page of the app')
def step_then_i_should_see_main_page_of_app(context):
    main_page_element = context.driver.find_element(AppiumBy.CLASS_NAME, "product_label")
    assert main_page_element.is_displayed(), "Main page not displayed"
    context.driver.quit()
