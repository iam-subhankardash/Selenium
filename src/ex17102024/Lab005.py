import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


def test_selenium_negative_with_class_name():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    user_name = driver.find_element(By.ID, "login-username")
    user_name.send_keys("admin")
    password = driver.find_element(By.ID, "login-password")
    password.send_keys("password")
    login_button = driver.find_element(By.ID, "js-login-btn")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message.text)
    #assert error_message.text == 'Your email, password, IP address or location did not match'
