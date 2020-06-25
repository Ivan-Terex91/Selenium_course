from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_css_selector("#treasure")
    x_value = treasure.get_attribute("valuex")
    x = calc(x_value)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(x)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button_submit = browser.find_element_by_css_selector(".btn")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
