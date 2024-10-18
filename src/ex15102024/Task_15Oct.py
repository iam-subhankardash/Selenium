from selenium import webdriver
import allure
import pytest


@pytest.mark.demo
@allure.title("Create a Selenium Script to verify the title")
def test_katalon_demo():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    current_title = driver.title
    print(current_title)
    print(current_url)
    source = driver.page_source
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert current_title == "CURA Healthcare Service"
    assert current_title in source

