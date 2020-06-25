from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys("Ivan")
    lastname = browser.find_element_by_css_selector('[name="lastname"]')
    lastname.send_keys("Terehin")
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("ITerex91@yandex.ru")
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.txt")
    upload_btn = browser.find_element_by_css_selector('[type="file"]')
    upload_btn.send_keys(file_path)
    button = browser.find_element_by_css_selector(".btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
