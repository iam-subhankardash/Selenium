# ChromeOptions -
# Some extra functionalities that you can do, before opening the Chrome
# 1. Start the browser in private mode - incognito
# 2. start the browse in headless - No UI (which will fast execution)
# 3. start the browser with the - maximize or minimize option
# 4. start the browser with the Window Size.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")  # Execution will not visible. It will run in background.

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

