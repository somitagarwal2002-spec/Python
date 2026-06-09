from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

MY_TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/P1QWmvKBqm-EpPIDpe2uzrckPsQh1_i1"
MY_EMAIL = "somit@gmail.com"
MY_PASSWORD = "somit@123"

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(MY_TINDOG_URL)

create_account = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH,"/html/body/section[1]/div[2]/a" ))
)
create_account.click()

facebook_login = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]'))
)
facebook_login.click()

base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

facebook_email_fillup = driver.find_element(By.ID, value="email")
facebook_email_fillup.send_keys(MY_EMAIL)

facebook_password_fillup = driver.find_element(By.ID, value="pass")
facebook_password_fillup.send_keys(MY_PASSWORD)
facebook_password_fillup.send_keys(Keys.ENTER)

time.sleep(2)

driver.switch_to.window(base_window)

location_access = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button'))
)
location_access.click()

enable_notifications = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button[1]'))
)
enable_notifications.click()

cookies_accept = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '//button[text()="I Accept"]'))
    # ec.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
)
cookies_accept.click()

for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value="btn-like")
        like_button.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)

driver.quit()
