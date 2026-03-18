from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

# Enter valid credentials
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Verify successful login message
success_message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))
)

print("Valid Login Test Executed Successfully")

driver.quit()
