from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_css_selector("#num1")
    num1_value = num1.text
    num2 = browser.find_element_by_css_selector("#num2")
    num2_value = num2.text
    dropdown_menu = Select(browser.find_element_by_css_selector("#dropdown"))
    dropdown_menu.select_by_value(str(int(num1_value) + int(num2_value)))
    button = browser.find_element_by_css_selector(".btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
