import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.alerts
@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_verify_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    # Click on alert button & check the result with assertion.
    js_alert_box = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    js_alert_box.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    result_message = driver.find_element(By.ID, "result").text
    assert result_message == "You successfully clicked an alert"
    time.sleep(5)


def test_verify_confirm_ok():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    js_confirm_box = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    js_confirm_box.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    result_message = driver.find_element(By.ID, "result").text
    assert result_message == "You clicked: Ok"
    time.sleep(5)


def test_verify_confirm_cancel():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    js_confirm_box = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    js_confirm_box.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    result_message = driver.find_element(By.ID, "result").text
    assert result_message == "You clicked: Cancel"
    time.sleep(5)


def test_verify_prompt_cancel():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    js_prompt_box = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_prompt_box.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    cancel_message = driver.find_element(By.ID, "result")
    assert cancel_message.text == "You entered: null"
    time.sleep(5)


def test_verify_prompt_ok():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    js_prompt_box = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_prompt_box.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Subhankar Dash")
    alert.accept()
    ok_message = driver.find_element(By.ID, "result").text
    assert ok_message == "You entered: Subhankar Dash"
    time.sleep(5)
