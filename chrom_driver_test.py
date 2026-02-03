from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Автоматически скачать и использовать подходящий ChromeDriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Пример действия: открыть сайт
driver.get("https://example.com")
print(driver.title)

# Закрыть браузер
driver.quit()
a = 123


