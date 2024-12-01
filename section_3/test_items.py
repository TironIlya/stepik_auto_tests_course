import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service(ChromeDriverManager().install())  # Создание объекта Service с путем к драйверу
    browser = webdriver.Chrome(service=service)  # Передача сервиса в webdriver
    yield browser
    browser.quit()

# Тест, который проверяет, что на странице товара есть кнопка "Добавить в корзину"
def test_add_to_cart_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    
    # Поиск кнопки "Add to cart" на странице
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверка, что кнопка существует
    assert button.is_displayed(), "Кнопки не видно"
