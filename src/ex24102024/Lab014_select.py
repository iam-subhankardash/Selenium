from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.alerts
@allure.title("Select")
@allure.description("Verify Select in dropdown")
def test_verify_select():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()

    select_html_tag = driver.find_element(By.XPATH, "//select[@id='dropdown']")
    select = Select(select_html_tag)
    select.select_by_visible_text("Option 2")
