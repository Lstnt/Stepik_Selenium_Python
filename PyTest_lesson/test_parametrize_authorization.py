from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

def test_authorization(browser,hidden):
    logmail,pasmail=hidden
    browser.get(link)
    browser.implicitly_wait(10)

    #Нажимает по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, "a.navbar__auth.navbar__auth_login").click()
    #Вводим данные для авторизации
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(logmail)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(pasmail)
    #Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()


    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button.navbar__profile-toggler")))
