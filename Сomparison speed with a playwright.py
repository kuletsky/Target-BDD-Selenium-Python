import time
start_time = time.time()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the SignIn page
driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element(By.CSS_SELECTOR, '#username').click()
driver.find_element(By.CSS_SELECTOR, '#username').send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, '#password').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()

assert 'Welcome' in driver.find_element(By.CSS_SELECTOR, ".subheader").text, f"Expected query not"

end_time = time.time()
end_time = end_time - start_time
print(f"Finished in {round(end_time, 2)} seconds.")


