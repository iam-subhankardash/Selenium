import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By

pytest.mark.partiallinktext


@allure.title("Positive Test case : Verify Start Free Trial")
@allure.description("Verify the anchor tag with partial link text")
def test_selenium_partial_link_text():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # Link text = exact match
    # Partial Link text = contains

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;
    # utm_source=login-page&amp;
    # utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>
    anchor_tag_link = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_link.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

