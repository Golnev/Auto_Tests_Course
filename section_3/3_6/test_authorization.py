import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from source import logs


link = 'https://stepik.org/lesson/236895/step/1'


@pytest.fixture
def log_in_stepic(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#ember33'))
    )
    login_button.click()

    browser.find_element(By.ID, 'id_login_email').send_keys(logs.login)
    browser.find_element(By.ID, 'id_login_password').send_keys(logs.password)

    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()

    return browser


def test_parametrisation_test(log_in_stepic):
    log_in_stepic.find_element(By.CSS_SELECTOR, '.navbar__profile-img')
