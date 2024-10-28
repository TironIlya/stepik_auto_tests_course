from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(v):
    return str(math.log(abs(12 * math.sin(int(v)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    v_element = select_element.get_attribute("valuex")
    v = v_element
    y = calc(v)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    submit = browser.find_element(
        By.CSS_SELECTOR, "body > div > form > div > div > button"
    )
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
