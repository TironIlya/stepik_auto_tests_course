import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


# Вычисление ответа
def calculate_answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service(ChromeDriverManager().install())  # Создание объекта Service с путем к драйверу
    browser = webdriver.Chrome(service=service)  # Передача сервиса в webdriver
    yield browser
    browser.quit()


# Функция для клика с обработкой ошибок
def click_element_with_retry(browser, locator, retries=3, timeout=10):
    for _ in range(retries):
        try:
            element = WebDriverWait(browser, timeout).until(EC.presence_of_element_located(locator))
            element.click()
            return
        except StaleElementReferenceException:
            print("Элемент стал устаревшим, повторная попытка...")
            time.sleep(1)  # Подождать 1 секунду перед повторной попыткой
        except TimeoutException:
            print(f"Время ожидания элемента истекло для локатора {locator}")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break
    print("Не удалось кликнуть по элементу после нескольких попыток.")


# Функция для ввода текста в элемент с обработкой ошибок
def send_keys_with_retry(browser, locator, text, retries=3, timeout=10):
    for _ in range(retries):
        try:
            element = WebDriverWait(browser, timeout).until(EC.presence_of_element_located(locator))
            element.clear()  # Очищаем поле перед вводом текста
            element.send_keys(text)
            return
        except StaleElementReferenceException:
            print("Элемент стал устаревшим, повторная попытка...")
            time.sleep(1)
        except TimeoutException:
            print(f"Время ожидания элемента истекло для локатора {locator}")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break
    print("Не удалось ввести текст в элемент после нескольких попыток.")


# Список ссылок для теста
@pytest.mark.parametrize("links", [
    "236895", "236896", "236897", "236898",
    "236899", "236903", "236904", "236905"
])
def test_stepik_task(browser, links):
    # Переменная для сбора фидбеков
    feedback_message = ""

    # Открытие страницы
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)

    # Ожидание и нажатие на ссылку "Войти"
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Войти")))

    # Ожидание исчезновения модального окна (если оно есть)
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog-bg")))

    # Клик на "Войти"
    login_button_locator = (By.LINK_TEXT, "Войти")
    click_element_with_retry(browser, login_button_locator)

    # Авторизация
    send_keys_with_retry(browser, (By.CSS_SELECTOR, "#id_login_email"), "admin@gmail.com")
    send_keys_with_retry(browser, (By.CSS_SELECTOR, "#id_login_password"), "admintest")

    # Клик по кнопке входа
    submit_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    click_element_with_retry(browser, submit_button_locator)

    time.sleep(5)

    # Ожидание загрузки страницы с задачей
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea")))

    time.sleep(5)

    # Очистка поля ввода и ввод ответа
    textarea_locator = (By.CSS_SELECTOR, "textarea.string-quiz__textarea")
    send_keys_with_retry(browser, textarea_locator, calculate_answer())

    time.sleep(5)

    # Нажатие кнопки "Отправить"
    submit_button_locator = (By.CSS_SELECTOR, "button.submit-submission")
    click_element_with_retry(browser, submit_button_locator)

    time.sleep(5)

    # Ожидание фидбека
    feedback_locator = (By.CSS_SELECTOR, ".smart-hints__hint")
    feedback = WebDriverWait(browser, 20).until(EC.presence_of_element_located(feedback_locator))
    feedback_text = feedback.text

    # Проверка текста фидбека
    if feedback_text != "Correct!":
        feedback_message += feedback_text

    assert feedback_text == "Correct!", f"Неверный фидбек: '{feedback_text}'"

    print(f"Фрагмент фидбека: {feedback_message}")


if __name__ == "__main__":
    pytest.main()
