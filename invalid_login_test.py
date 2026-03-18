from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

# Enter invalid credentials
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpassword")

# Click Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Verify error message
error_message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))
)

print("Invalid Login Test Executed Successfully")

driver.quit()