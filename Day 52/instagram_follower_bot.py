from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException 
import time

SIMILAR_ACCOUNT = "chefsteps"   
USERNAME = "selenium_python_"       
PASSWORD = "Somit@0987654321"   
BASE_URL = "https://www.instagram.com/" 
LOGIN_URL = f"{BASE_URL}accounts/login/?hl=en"

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

condition = True

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(LOGIN_URL)

    def login(self):
        username_fillup = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="_R_32d9lplcldcpbn6b5ipamH1_"]'))
        )
        username_fillup.send_keys(USERNAME)

        password_fillup = self.driver.find_element(By.XPATH, value='//*[@id="_R_33d9lplcldcpbn6b5ipamH1_"]')
        # password_fillup.click()
        password_fillup.send_keys(PASSWORD)

        login_click = self.driver.find_element(By.XPATH, value='//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div')
        login_click.click()

        not_now = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]"))
        )
        if not_now:
            not_now.click()

        notifications_off = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Not Now')]"))
        )
        if notifications_off:
            notifications_off.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        
        time.sleep(6)

        followers_click =  WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
        (By.XPATH, "//a[contains(.,'followers')]"))
        )
        followers_click.click()

        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(10)
        all_buttons = self.driver.find_elements(By.XPATH, value="//button[contains(text(), 'Follow')]")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
