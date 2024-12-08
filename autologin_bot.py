from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service("C:/Users/Dushyant Khandelwal/Desktop/autoLogin/chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:

    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(2)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.send_keys("dushyant.fr")
    password.send_keys("/////")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(5)

    if driver.current_url == "https://www.instagram.com/":
        print("Login successful!")
    else:
        print("Login failed. Check your credentials or check for CAPTCHA.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:

    driver.quit()
