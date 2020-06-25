from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_trol = browser.find_element_by_css_selector(".trollface")
    button_trol.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector("#input_value")
    x_value = x.text
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(calc(x_value))
    btn_prm = browser.find_element_by_css_selector(".btn")
    btn_prm.click()
finally:
    time.sleep(10)
    browser.quit()