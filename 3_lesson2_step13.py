import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

class TestStepik(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_registration1(self):
        # Открываем первую страницу регистрации
        self.driver.get(link_1)

        # Заполняем поля формы
        input1 = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("abcd@email.com")

        # Нажимаем кнопку отправки
        button = self.driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем появления заголовка об успешной регистрации
        welcome_text_elt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        welcome_text = welcome_text_elt.text

        # Проверяем, что текст содержит строку о успешной регистрации
        self.assertIn("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        # Открываем вторую страницу регистрации
        self.driver.get(link_2)

        # Заполняем поля формы
        input1 = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("abcd@email.com")

        # Нажимаем кнопку отправки
        button = self.driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем появления заголовка об успешной регистрации
        welcome_text_elt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        welcome_text = welcome_text_elt.text

        # Проверяем, что текст содержит строку о успешной регистрации
        self.assertIn("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
