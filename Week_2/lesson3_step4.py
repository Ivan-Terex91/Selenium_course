from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_css_selector("#input_value")
    x_value = x.text
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(calc(x_value))
    button_submit = browser.find_element_by_css_selector(".btn")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
