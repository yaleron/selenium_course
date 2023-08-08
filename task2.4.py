from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get('https://SunInJuly.github.io/execute_script.html')
    x = calc(int(browser.find_element(By.ID, 'input_value').text))
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(x)
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    radiobut = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radiobut)
    radiobut.click()
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
