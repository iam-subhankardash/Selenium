import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


def test_selenium_locator():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    time.sleep(2)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    user_name = driver.find_element(By.ID, "txt-username")
    user_name.send_keys("John Doe")
    time.sleep(2)
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    time.sleep(2)
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"