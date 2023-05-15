import math
import time

import pytest
from source import logs
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("lessons", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestAuth:
    def test_links(self, browser, lessons):
        browser.implicitly_wait(10)

        answer = str(math.log(int(time.time())))
        browser.get(f"https://stepik.org/lesson/{lessons}/step/1")
        browser.find_element(By.ID, "ember33").click()

        browser.find_element(By.ID, "id_login_email").send_keys(logs.login)

        browser.find_element(By.ID, "id_login_password").send_keys(logs.password)
        browser.find_element(By.CSS_SELECTOR, "#login_form > button").click()
        time.sleep(7)
        browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "div.attempt__actions > button").click()
        time.sleep(5)
        message = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
        assert message == "Correct!"
