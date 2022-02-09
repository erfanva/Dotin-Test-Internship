
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import config

s = Service('./driver/chromedriver') # Optional argument, if not specified will search path.
driver = webdriver.Chrome(service=s)  
driver.implicitly_wait(10)

driver.get('https://www.digikala.com/')

login_btn = driver.find_element(By.CSS_SELECTOR, "a[data-cro-id='header-profile']")
login_btn.click()

element = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
element.send_keys(config.email_or_phone)
element.submit()

element = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
element.send_keys(config.password)
element.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()