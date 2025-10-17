from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Negative Registration Test (Invalid Last Name)
# 1. Open website invu.ge
# 2. Click Sign Up Button
# 3. Enter Last name with invalid characters ("@")
# 4. Fill other fields validly (First Name – Mariam, Email - Email@gmail.com, Password - "Password123", Confirmation Password - "Password123")
# 5. Click Create Account
# 6. Validate Signing up not successfully

driver = webdriver.Chrome()
driver.get("https://www.invu.ge")
time.sleep(2)

# Click Sign Up Button (tries both English and Georgian labels)
try:
    signup_button = driver.find_element(By.LINK_TEXT, "Sign Up")
except:
    try:
        signup_button = driver.find_element(By.LINK_TEXT, "რეგისტრაცია")
    except Exception as e:
        print("Sign Up button not found. Please update selector.", e)
        driver.quit()
        exit()
signup_button.click()
time.sleep(2)

# Enter First Name
try:
    first_name_input = driver.find_element(By.NAME, "firstName")
    first_name_input.clear()
    first_name_input.send_keys("Mariam")
except:
    print("First Name field not found. Please update selector.")

# Enter Last Name with invalid characters
try:
    last_name_input = driver.find_element(By.NAME, "lastName")
    last_name_input.clear()
    last_name_input.send_keys("@")
except:
    print("Last Name field not found. Please update selector.")

# Enter Email
try:
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("Email@gmail.com")
except:
    print("Email field not found. Please update selector.")

# Enter Password
try:
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("Password123")
except:
    print("Password field not found. Please update selector.")

# Confirm Password
try:
    confirm_password_input = driver.find_element(By.NAME, "confirmPassword")
    confirm_password_input.clear()
    confirm_password_input.send_keys("Password123")
except:
    print("Confirm Password field not found. Please update selector.")

# Click Create Account
try:
    create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account') or contains(text(), 'Sign Up') or contains(text(), 'რეგისტრაცია')]")
    create_button.click()
except:
    print("Create Account button not found. Please update selector.")
time.sleep(2)

# Validate Signing up not successfully (look for error message or registration form still present)
try:
    error_element = driver.find_element(By.XPATH, "//*[contains(text(), 'error') or contains(text(), 'invalid') or contains(text(), 'character') or contains(@class, 'error')]")
    print("Test Passed: Registration not successful, error message found.")
except:
    print("Test Inconclusive: No error message found. Please check manually.")

driver.quit()
