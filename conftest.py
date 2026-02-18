import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def hidden():
    with open("mail.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines[0], lines[1]
