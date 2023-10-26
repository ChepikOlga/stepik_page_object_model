import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def find_button(browser):
    try:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, ".//button[@type='submit']")))
        return True
    except TimeoutException:
        return False

def test_add_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert find_button(browser)


if __name__ == "__main__":
    unittest.main()
