import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('number',["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_authorization(browser,hidden,number):
    logmail,pasmail=hidden
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(20)

    #Нажимает по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, "a.navbar__auth.navbar__auth_login").click()
    #Вводим данные для авторизации
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(logmail)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(pasmail)
    #Отправляем форму для авторизации
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()

    #Вводим ответы и отправляем
    answer = math.log(int(time.time()))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area.string-quiz__textarea")))
    browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area.string-quiz__textarea").send_keys(answer)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))

    browser.find_element(By.CSS_SELECTOR,"button.submit-submission").click()

    fitback = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))

    assert fitback.text == "Correct!",f'Ответ не принят по причине {fitback.text}'