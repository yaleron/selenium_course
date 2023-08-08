from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get(' http://suninjuly.github.io/cats.html')
    browser.find_element(By.ID, 'button')
finally:
    browser.quit()


    