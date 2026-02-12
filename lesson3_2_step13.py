import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestReg(unittest.TestCase):
    def test_registration_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, 'input[required].first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, 'input[required].second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, 'input[required].third')
            input3.send_keys("Test@ya.com")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)
            # Явное ожидание заголовка
            welcome_text_elt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            answer = "Congratulations! You have successfully registered!"
            # с помощью assert(в стиле unittest) проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text,answer,
                         "Регистрация на сайте провалилась")
        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, 'input[required].first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, 'input[required].second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, 'input[required].third')
            input3.send_keys("Test@ya.com")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)
            # Явное ожидание заголовка
            welcome_text_elt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            welcome_text = welcome_text_elt.text

            # с помощью assert(в стиле unittest) проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                             "Регистрация на сайте провалилась")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()