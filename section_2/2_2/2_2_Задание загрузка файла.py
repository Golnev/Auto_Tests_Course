import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    last_name = browser.find_element(By.NAME, 'lastname')
    email = browser.find_element(By.NAME, 'email')

    first_name.send_keys('Eugene')
    last_name.send_keys('Golnev')
    email.send_keys('test@gmail.com')

    attach = browser.find_element(By.ID, 'file')
    attach.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
