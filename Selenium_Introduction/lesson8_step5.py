from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #Считываем значение x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    #Вводим полученный ответ
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    #Проскроллим (разные варианты)
    #browser.execute_script("window.scrollBy(0, 100);")

    #Отмечаем чекбокс и переключатель
    options1 = browser.find_element(By.ID, 'robotCheckbox')
    options1.click()
    options2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("arguments[0].scrollIntoView(true);", options2)
    options2.click()

    #Отправляем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()