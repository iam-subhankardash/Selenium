import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.explicitwait
@allure.title("Explicit Wait")
@allure.description("Verify the explicit wait")
def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_address = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_address.send_keys("abcd@gmail.com")
    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("xyz123")
    signin_button = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    signin_button.click()
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))
    time.sleep(5)
