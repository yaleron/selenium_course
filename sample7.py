from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = calc(int(browser.find_element(By.ID, 'input_value').text))
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(x)
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()


