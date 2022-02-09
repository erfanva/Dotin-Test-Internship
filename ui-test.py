
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import config

s = Service('./driver/chromedriver') # Optional argument, if not specified will search path.
driver = webdriver.Chrome(service=s)  
driver.implicitly_wait(10)

# open main page
driver.get('https://www.digikala.com/')

### login stage
# go to login page
login_btn = driver.find_element(By.CSS_SELECTOR, "header a[data-cro-id='header-profile']")
login_btn.click()

# enter username and submit
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username_input.send_keys(config.email_or_phone)
username_input.submit()

# enter password and submit
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password_input.send_keys(config.password)
password_input.submit()

### get user informations stage
# open profile drop down
profile_icon = driver.find_element(By.CSS_SELECTOR, "header div[class*='profile']")
profile_icon.click()

# find the name
name = driver.find_element(By.CSS_SELECTOR, "header a[data-cro-id='header-profile-detail']")
print("Name:", name.text)
assert name.text == config.name, "Name is incorrect"


time.sleep(5) # Let the user actually see something!

driver.quit()