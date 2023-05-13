import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def operation(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

browser.implicitly_wait(3)

try:
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    browser.find_element(By.ID, 'book').click()

    x_str = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(operation(x_str))

    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    browser.quit()
