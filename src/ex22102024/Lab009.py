import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.mark.ebay
@allure.title("ebay automation")
@allure.description("Search all macbook mini options & get the details")
def test_ebay_automation():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    driver.maximize_window()
    time.sleep(2)
    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_box.send_keys("Macmini")
    time.sleep(2)
    search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()
    list_of_items = driver.find_elements(By.CSS_SELECTOR, "span[role='heading']")
    for i in list_of_items:
        print(i.text)

    price_of_items = driver.find_elements(By.CSS_SELECTOR, 'span[class="s-item__price"]')
    for p in price_of_items:
        print(p.text)
