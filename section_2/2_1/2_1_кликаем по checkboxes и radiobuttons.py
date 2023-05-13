import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radiobutton = browser.find_element(By.ID, 'robotsRule')

    checkbox.click()
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
