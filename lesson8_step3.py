from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def calc(x,y):
    return str(int(x)+int(y))

try:
    link = "https://suninjuly.github.io/selects1.html" #работает и для http://suninjuly.github.io/selects2.html
    browser = webdriver.Chrome()
    browser.get(link)


    #Считываем значение x и y
    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    s = calc(x,y)

    #Находим в списке подходящий вариант
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s)

    #Отправляем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()