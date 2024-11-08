from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = b_element.text

    sum = int(a) + int(b)

    browser.find_element(By.CSS_SELECTOR, (f"[value='{sum}']")).click()

    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
