from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

# Read the HTML file
with open('pending_follow_requests.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
instagram_profile_links = soup.find_all('a', {'target': '_blank'})
usernames = [link.text for link in instagram_profile_links]

# Setup WebDriver
options = Options()
options.add_experimental_option("detach", True)
service = Service('/usr/local/bin/chromedriver') 
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://www.instagram.com/')
time.sleep(2)

# Log in to Instagram
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5)

# Process each username
for username in usernames:
    try:
        print(f"Processing {username}...")
        driver.get(f'https://instagram.com/{username}/')
        time.sleep(5)

        # Interact with the "Requested" button
        requested_button = driver.find_element(By.XPATH, "//button[@type='button']")
        requested_button.click()
        time.sleep(2)

        # Confirm action
        confirm_button = driver.find_element(By.CLASS_NAME, '_a9--')
        confirm_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred with {username}: {e}")

# Close the driver
driver.quit()
