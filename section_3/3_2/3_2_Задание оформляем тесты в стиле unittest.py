import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def inputs(browser):
    input_1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input_1.send_keys('test.txt')

    input_2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input_2.send_keys('test.txt')

    input_3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input_3.send_keys('test.txt')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text

    return welcome_text


class TestLink(unittest.TestCase):
    def test_link_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        welcome_text = inputs(browser)
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', f'expected {welcome_text}')
        browser.quit()

    def test_link_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        welcome_text = inputs(browser)
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', f'expected {welcome_text}')
        browser.quit()


if __name__ == '__main__':
    unittest.main()
