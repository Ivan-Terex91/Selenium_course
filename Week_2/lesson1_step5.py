from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    result = calc(x)
    input_result = browser.find_element_by_css_selector("#answer")
    input_result.send_keys(result)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button_submit = browser.find_element_by_css_selector(".btn")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
