from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #Считываем значение x под картинкой сундука
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    #Вводим полученный ответ
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    #Отмечаем чекбокс и переключатель
    options1 = browser.find_element(By.ID, 'robotCheckbox')
    options1.click()
    options2 = browser.find_element(By.ID, 'robotsRule')
    options2.click()

    #Отправляем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()