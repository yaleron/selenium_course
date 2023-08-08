from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = calc(int(browser.find_element(By.ID, 'input_value').text))
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(x)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()