import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


@pytest.mark.html
@allure.title("HTML page practice")
@allure.description("Practice for Radio, Checkbox")
def test_radio_textbox():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys("Shubham")
    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys("Dash")
    gender = driver.find_element(By.ID, "sex-1")
    gender.click()
    exp = driver.find_element(By.ID, "exp-2")
    exp.click()
    profession = driver.find_element(By.CSS_SELECTOR, "input#profession-1")
    profession.click()
    time.sleep(5)
