from selenium import webdriver


def test_open_vwo_login():
    driver = webdriver.Chrome()
    # POST request to create a fresh copy of Chrome
    # A fresh session ID will be created
    driver.get("https://app.vwo.com")
    print(driver.title)  # Get request
    assert driver.title == "Login - VWO"
