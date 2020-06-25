from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
