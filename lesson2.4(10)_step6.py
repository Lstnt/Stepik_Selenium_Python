import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) #Добавим неявное ожидание
    browser.get(link)

    #Добавляем явное ожидание цены в 100
    wait = WebDriverWait(browser, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID,'price'),"$100"))
    book = browser.find_element(By.ID,'book')
    book.click()


    #Считываем значение x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    #Вводим полученный ответ
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    #Отправляем
    button = browser.find_element(By.ID, 'solve')
    button.click()



finally:
    # Копируем ответ в буфер
    alert = browser.switch_to.alert
    CopyAnswer = alert.text.split(': ')
    pyperclip.copy(CopyAnswer[1])
    alert.accept()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()