import time

from selenium import webdriver
import pytest
import allure


def test_Edge():
    driver = webdriver.Edge()
    driver.get("https://www.udemy.com/")
    driver.maximize_window()
    time.sleep(5)


def test_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.udemy.com/")
    driver.maximize_window()
    time.sleep(5)


def test_Firefox():
    driver = webdriver.Firefox()
    driver.get("https://www.udemy.com/")
    driver.maximize_window()
    time.sleep(5)

# -n auto --> automatically decide how many parallel we want to execute
