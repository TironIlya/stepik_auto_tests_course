from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    input1.send_keys("Ilya")
    input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    input2.send_keys("tiron@gmail.com")
    input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    input3.send_keys("test@email.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    send = browser.find_element(By.CSS_SELECTOR, "#file")
    send.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
