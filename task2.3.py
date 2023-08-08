from selenium.webdriver.support.ui import Select
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/selects1.html")
    sum = str(int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
finally:
    time.sleep(20)
    browser.quit()