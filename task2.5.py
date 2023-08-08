from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By.NAME, 'firstname').send_keys('lero')
    browser.find_element(By.NAME, 'lastname').send_keys('kholod')
    browser.find_element(By.NAME, 'email').send_keys('yaleronn@gmail.com')
    file = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'task.txt')
    file.send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()