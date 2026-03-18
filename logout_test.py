from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open Login Page
driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

# Step 3: Login First (Required before Logout)
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Step 4: Click Logout Button
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius"))).click()

# Step 5: Verify Logout Success Message
message = wait.until(EC.presence_of_element_located((By.ID, "flash")))

if "You logged out of the secure area!" in message.text:
    print("Logout Test Passed ✅")
else:
    print("Logout Test Failed ❌")

# Step 6: Close Browser
driver.quit()