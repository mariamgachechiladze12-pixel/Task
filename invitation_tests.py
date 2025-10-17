from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.invu.ge")
time.sleep(4)

# Click Login Button
try:
    login_button = driver.find_element(By.LINK_TEXT, "Login")
except Exception as e:
    print("Login button not found:", e)
    login_button = driver.find_element(By.LINK_TEXT, "შესვლა")
login_button.click()
time.sleep(4)

# Enter email and password
email_input = driver.find_element(By.NAME, "email")
email_input.clear()
email_input.send_keys("dressup118@gmail.com")
password_input = driver.find_element(By.NAME, "password")
password_input.clear()
password_input.send_keys("1111111111111111111")

# Click Sign In
sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In') or contains(text(), 'Log In') or contains(text(), 'Login') or contains(text(), 'შესვლა')]")
sign_in_button.click()
time.sleep(5)

# Choose Template
try:
    templates_link = driver.find_element(By.LINK_TEXT, "Templates")
    templates_link.click()
except Exception as e:
    print("Templates link not found:", e)
    templates_link = driver.find_element(By.LINK_TEXT, "შაბლონები")
    templates_link.click()
time.sleep(4)

# Pick Minimal Birthday
minimal_birthday = driver.find_element(By.XPATH, "//h3[contains(@class, 'font-semibold') and contains(text(), 'Minimal Birthday')]")
minimal_birthday.click()
time.sleep(4)

# Enter Event Title
event_title = driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='მაგალითად, ემა და ნოას ქორწილი']")
event_title.clear()
event_title.send_keys("MG Birthday")

# Enter Past Event Date
event_date = driver.find_element(By.XPATH, "//input[@type='date']")
event_date.clear()
event_date.send_keys("2024-10-17")

# Click Create Invitation
create_button = None
try:
    # Try class-based selector first
    create_button = driver.find_element(By.XPATH, "//button[@class='flex-1 bg-gradient-to-r from-primary-500 to-secondary-500 hover:from-primary-600 hover:to-secondary-600 disabled:from-gray-400 disabled:to-gray-500 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105 disabled:hover:scale-100 disabled:cursor-not-allowed']")
    create_button.click()
except Exception as e:
    print("Class-based button not found:", e)
    try:
        create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Invitation') or contains(text(), 'მოსაწვევის შექმნა')]")
        create_button.click()
    except Exception as e:
        print("Text-based button not found:", e)

# Check for error/validation message (example selector, update as needed)
try:
    error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'თარიღი არასწორია') or contains(text(), 'Invalid date')]")
    print("Validation message found:", error_message.text)
    time.sleep(2)
except Exception as e:
    print("No validation message found. Please check manually.", e)
    time.sleep(2)

driver.quit()
