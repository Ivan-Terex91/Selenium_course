import unittest
import time
from selenium import webdriver


class TestClass(unittest.TestCase):
    def test_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Код, который заполняет обязательные поля
        input_firstname = browser.find_element_by_css_selector(".first_block input.first")
        input_firstname.send_keys("Ivan")
        input_secodname = browser.find_element_by_css_selector(".first_block input.second")
        input_secodname.send_keys("Terehin")
        input_email = browser.find_element_by_css_selector(".first_block input.third")
        input_email.send_keys("Valerievich")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(3)

        welcome_text_elm = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elm.text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, welcome_text,
                         f"Ожидаемый результат '{expected_text}', полученный результат '{welcome_text}'")
        time.sleep(5)
        browser.quit()


if __name__ == 'main':
    unittest.main()
    # testing = TestClass()
    # links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
    # for link in links:
    #     testing.test_page(link=link)
