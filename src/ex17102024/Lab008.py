import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.mark.registration
@allure.title("Registration Page Automation")
@allure.description("Automation for the Registration Page of the AwesomeQA.com/UI")
def test_registration_page_automation():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.maximize_window()
    first_name_input_box = driver.find_element(By.ID, "input-firstname")
    first_name_input_box.send_keys("Subhankar")
    time.sleep(2)
    last_name_input_box = driver.find_element(By.NAME, "lastname")
    last_name_input_box.send_keys("Dash")
    time.sleep(2)
    email_input_box = driver.find_element(By.XPATH, "//input[@id='input-email']")
    email_input_box.send_keys("isubhankar2@gmail.com")
    time.sleep(2)
    telephone_input_box = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    telephone_input_box.send_keys("1234567890")
    time.sleep(2)
    password_input_box = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password_input_box.send_keys("project123")
    time.sleep(2)
    password_confirm_input_box = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    password_confirm_input_box.send_keys("project123")
    time.sleep(2)
    privacy_policy_box = driver.find_element(By.XPATH, "//input[@name='agree']")
    privacy_policy_box.click()
    time.sleep(2)
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    time.sleep(5)
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    source_page = driver.page_source
    assert "Your Account Has Been Created!" in source_page
