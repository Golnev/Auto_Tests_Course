import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def operation(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    browser.switch_to.alert.accept()

    x_str = browser.find_element(By.ID, 'input_value').text

    browser.find_element(By.ID, 'answer').send_keys(operation(x_str))

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
