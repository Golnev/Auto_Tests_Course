import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLink(unittest.TestCase):
    browser = webdriver.Chrome()

    def inputs(self):
        input_1 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input_1.send_keys('test.txt')

        input_2 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input_2.send_keys('test.txt')

        input_3 = self.browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input_3.send_keys('test.txt')

        button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text = self.browser.find_element(By.TAG_NAME, 'h1').text

        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', f'expected {welcome_text}')

    def test_link_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.browser.get(link)

        self.inputs()

    def test_link_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.browser.get(link)

        self.inputs()


if __name__ == '__main__':
    unittest.main()
