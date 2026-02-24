import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= "en", help='Выберите язык: ru, en, es, fr и т.д.')




@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    browser = None
    print(f"\nstart chrome browser for test,language:{language}")
    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def hidden():
    with open("mail.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines[0], lines[1]
