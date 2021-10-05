import unittest
from  selenium import webdriver
import time

class Test(unittest.TestCase):
    def test_squad1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_tag_name("div.first_block .form-control.first")
            input1.send_keys("Yana")
            input2 = browser.find_element_by_tag_name("div.first_block .form-control.second")
            input2.send_keys("Antonovich")
            input2 = browser.find_element_by_tag_name("div.first_block .form-control.third")
            input2.send_keys("ololo@mail.ru")
	
            time.sleep(1) #этот слип добавил сам, чтоб видеть как заполняет поля.
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_squad2(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_tag_name("div.first_block .form-control.first")
            input1.send_keys("Yana")
            input2 = browser.find_element_by_tag_name("div.first_block .form-control.second")
            input2.send_keys("Antonovich")
            input2 = browser.find_element_by_tag_name("div.first_block .form-control.third")
            input2.send_keys("ololo@mail.ru")

            time.sleep(3) #этот слип добавил сам, чтоб видеть как заполняет поля.
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(3)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed")
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
if __name__ == "__main__":
    unittest.main()