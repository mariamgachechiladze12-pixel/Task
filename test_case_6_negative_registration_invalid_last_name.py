from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test data
FIRST_NAME = "Mariam"
LAST_NAME = "@"
EMAIL = "Email@gmail.com"
PASSWORD = "Password123"

# Start WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait_time = 3

try:
    # 1. Open website invu.ge
    driver.get("https://invu.ge")
    time.sleep(wait_time)


    # 2. Click Sign In Button (try multiple selectors)
    try:
        sign_in_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In') or contains(text(), 'შესვლა') or contains(text(), 'Login')]")
    except Exception as e:
        print("Sign In button not found:", e)
        sign_in_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In') or contains(text(), 'შესვლა') or contains(text(), 'Login')]")
    sign_in_btn.click()
    time.sleep(wait_time)

    # 3. Enter Last name with invalid characters
    last_name_input = driver.find_element(By.NAME, "lastName")
    last_name_input.clear()
    last_name_input.send_keys(LAST_NAME)

    # 4. Fill other fields validly
    first_name_input = driver.find_element(By.NAME, "firstName")
    first_name_input.clear()
    first_name_input.send_keys(FIRST_NAME)

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys(EMAIL)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(PASSWORD)

    confirm_password_input = driver.find_element(By.NAME, "confirmPassword")
    confirm_password_input.clear()
    confirm_password_input.send_keys(PASSWORD)


    # 5. Click Create Account
    try:
        create_account_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account') or contains(text(), 'ანგარიშის შექმნა') or contains(text(), 'Register')]")
    except Exception as e:
        print("Create Account button not found:", e)
        create_account_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Create Account') or contains(text(), 'ანგარიშის შექმნა') or contains(text(), 'Register')]")
    create_account_btn.click()
    time.sleep(wait_time)

    # 6. Validate Signing up not successfully (look for error message)
    try:
        error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid last name') or contains(text(), 'გვარი არასწორია')]")
        print("Validation message found:", error_message.text)
    except Exception as e:
        print("No validation message found. Please check manually.", e)
finally:
    driver.quit()
