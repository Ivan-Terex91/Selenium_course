from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_book = browser.find_element_by_css_selector("#book")
    needed_price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")
                                                   )
    button_book.click()
    x = browser.find_element_by_css_selector("#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x_value = x.text
    answer = browser.find_element_by_css_selector("#answer")
    # browser.execute_script("return[0].")
    answer.send_keys(calc(x_value))
    button_submit = browser.find_element_by_css_selector("#solve")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
