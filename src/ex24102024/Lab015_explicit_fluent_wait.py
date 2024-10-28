import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@pytest.mark.explicitwait
@allure.title("Explicit Wait with Fluent wait")
@allure.description("Verify the explicit wait along with fluent wait")
def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    search = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    search.send_keys("The Testing Academy")
    enter_key = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
    enter_key.click()
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    # Fluent Wait
    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='https://thetestingacademy.com/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='The Testing Academy']")))
    time.sleep(2)
