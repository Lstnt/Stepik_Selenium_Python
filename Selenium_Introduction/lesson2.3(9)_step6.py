import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем первую кнопку
    onebutton = browser.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    onebutton.click()

    #Переключаемся на новое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
    # Копируем ответ в буфер
    alert = browser.switch_to.alert
    CopyAnswer = alert.text.split(': ')
    pyperclip.copy(CopyAnswer[1])
    alert.accept()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()