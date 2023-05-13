import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def operation(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_str_el = browser.find_element(By.ID, 'input_value')
    x_str = x_str_el.text
    browser.find_element(By.ID, 'answer').send_keys(operation(x_str))

    browser.execute_script("return arguments[0].scrollIntoView(true);", x_str_el)

    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()

    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
