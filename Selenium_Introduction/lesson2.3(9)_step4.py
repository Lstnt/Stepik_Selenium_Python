from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем первую кнопку
    onebutton = browser.find_element(By.CSS_SELECTOR, '[type=submit]')
    onebutton.click()

    #Принимаем модальное окно
    confirm = browser.switch_to.alert
    confirm.accept()

    #Считываем значение x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    #Вводим полученный ответ
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    #Отправляем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()