from os import getenv
from selenium import webdriver
import requests

BASE_URL = getenv('BASE_URL', 'http://127.0.0.1:5000')
WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))

def before_all(context):
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS

    # Instantiate the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=options)

    requests.post(f"{BASE_URL}/pets/reset")

def after_all(context):
    context.driver.quit()
