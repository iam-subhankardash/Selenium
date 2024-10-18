from selenium import webdriver
import allure
import pytest


@allure.title("Verify the title of webpage")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://onlinetraining.krnetworkcloud.org/")
    driver.maximize_window()
