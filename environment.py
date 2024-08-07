import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

def get_env_var(var_name, default=None):
    """
    Get an environment variable with a default value.
    """
    return os.getenv(var_name, default)

def is_headless():
    """
    Check if headless mode should be enabled based on environment variables.
    """
    return get_env_var("HEADLESS") == "true"


def get_browser_options():
    """
    Get browser options based on environment variables.
    """
    headless = is_headless()
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    if headless:
        options.add_argument("--headless")
    
    return options

def get_appium_config():
    """
    Get Appium configuration.
    """
    return {
        "appium_server_url": "http://127.0.0.1:4723",
        "platform_name": "Android",
        "device_name": "Android Emulator",
        "browser_name": "Chrome"
    }


def get_locust_config():
    """
    Get Locust configuration.
    """
    return {
        "host": "http://localhost:8080",
        "users": 10,
        "spawn_rate": 1,
        "run_time": 600
    }

def get_zap_config():
    """
    Get ZAP configuration.
    """
    return {
        "proxy": "http://localhost:8080"
    }

def get_axe_core_config():
    """
    Get Axe-Core configuration.
    """
    return {
        "rules": {
            "color-contrast": {
                "enabled": True
            },
            "duplicate-id": {
                "enabled": True
            },
        }
    }
