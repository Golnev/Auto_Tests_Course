import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, 'num1').text
    num_2 = browser.find_element(By.ID, 'num2').text

    sum_str = str(int(num_1) + int(num_2))

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(sum_str)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
