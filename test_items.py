import time

from selenium.webdriver.common.by import By


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item(browser):
    browser.get(url)
    time.sleep(10)
    button = len(browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, "Button is missing"
