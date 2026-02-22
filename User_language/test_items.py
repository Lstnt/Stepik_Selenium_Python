from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-primary.btn-add-to-basket")) > 0, \
        "Отсутствует кнопка добавления в корзину"