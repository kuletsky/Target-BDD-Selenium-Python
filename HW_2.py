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

# open the url
driver.get("https://www.target.com/")

# click SignIn button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(6)

# Verification
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert "Sign into your Target account" in actual_text, f"Error! {actual_text}"

sleep(1)

driver.find_element(By.ID, "login").click()
print("SIGNIN is successful!")

sleep(4)


# SEARCH ITEM
# open the url
driver.get("https://www.target.com/")
# enter "towels" in search field
driver.find_element(By.ID, "search").send_keys("towels")
# click search btn
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)

# Verification
search_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert "towels" in search_text, f"Error! {search_text}"
print("SEARCH is successful!")

driver.quit()
