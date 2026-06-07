from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

MY_NAME = "Somit Agarwal"
ACCOUNT_EMAIL = "somit@test.com"
ACCOUNT_PASSWORD = "somit@123"
GYM_URL = "https://appbrewery.github.io/gym/"

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

join_today_or_tomo = driver.find_element(By.CLASS_NAME, value="Home_heroButton__3eeI3")
join_today_or_tomo.click()

# time.sleep(2) iski jagah we are using webdriverwait

# start_register = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "toggle-login-register"))
# )
# start_register.send_keys(Keys.ENTER)

# time.sleep(2)

# register_name = driver.find_element(By.ID, value="name-input")
# register_name.send_keys(MY_NAME)

# register_email = driver.find_element(By.ID, value="email-input")
# register_email.send_keys(ACCOUNT_EMAIL)

# register_password = driver.find_element(By.ID, value="password-input")
# register_password.send_keys(ACCOUNT_PASSWORD)

# click_on_register = driver.find_element(By.ID, value="submit-button")
# click_on_register.click()

time.sleep(2)

wait = WebDriverWait(driver, 2)

login_email_input = driver.find_element(By.NAME, value="email")
login_email_input.send_keys(ACCOUNT_EMAIL)

login_password_input = driver.find_element(By.NAME, value="password")
login_password_input.send_keys(ACCOUNT_PASSWORD)

login_click = driver.find_element(By.ID, value="submit-button")
login_click.click()

wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, value="./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, value="h2").text

    if "Tue" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, value="p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, value="h3[id^='class-name-']").text

            button = card.find_element(By.CSS_SELECTOR, value="button[id^='book-button-']")
            button.click()

            print(f"✓ Booked: {class_name} on {day_title}")


