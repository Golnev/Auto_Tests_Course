import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/find_link_text'

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()

    input_1 = browser.find_element(By.TAG_NAME, 'input')
    input_1.send_keys('Eugene')

    input_2 = browser.find_element(By.NAME, 'last_name')
    input_2.send_keys('Golnev')

    input_3 = browser.find_element(By.CLASS_NAME, 'city')
    # input_3 = browser.find_element(By.NAME, 'firstname')
    input_3.send_keys('Wroclaw')

    input_4 = browser.find_element(By.ID, 'country')
    input_4.send_keys('Poland')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(19)
    browser.quit()
