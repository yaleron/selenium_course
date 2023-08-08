import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    field = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    field.send_keys(y)
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    rad_but = browser.find_element(By.ID, 'robotsRule')
    rad_but.click()
    sub_but = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    sub_but.click()
finally:
    time.sleep(10)
    browser.quit()