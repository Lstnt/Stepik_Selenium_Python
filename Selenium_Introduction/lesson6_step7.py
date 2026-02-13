from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from faker import Faker

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME,'input')
    for element in elements:
        #fake=Faker()
        lst=Faker().name()
        element.send_keys(lst)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
