from selenium import webdriver
from selenium.webdriver.common.by import By

import time


try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input_1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input_1.send_keys('test.txt')

    input_2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input_2.send_keys('test.txt')

    input_3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input_3.send_keys('test.txt')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(10)
    browser.quit()
