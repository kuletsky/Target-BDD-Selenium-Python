from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the SignIn page
driver.get('https://www.amazon.com/')
driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList-nav-line-1').click()
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()
# sleep(2)

# Check locators for Create Account on amazon.com
element = driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, "h1[class=a-spacing-small]")
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
element.send_keys()
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, "#ap_email")
element.send_keys()
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, "#ap_password")
element.send_keys()
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

# element = driver.find_element(By.CSS_SELECTOR, "[aria-live='polite']")
element = driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least 6 characters.')]")
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
element.send_keys()
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

driver.find_element(By.CSS_SELECTOR, "#continue.a-button-input")
# driver.execute_script("arguments[0].style.color = 'red'", element)

element = driver.find_element(By.CSS_SELECTOR, "a[href*='display.html/ref=ap_register_notification_condition_of_use']")
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, "a[href*='display.html/ref=ap_register_notification_privacy_notice']")
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

element = driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
driver.execute_script("arguments[0].style.border = '2px solid red'", element)

sleep(16)
driver.quit()