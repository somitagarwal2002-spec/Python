from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time 

PROMISED_DOWN = 150
PROMISED_UP = 10
Y_EMAIL = "somitagarwal2002@gmail.com"
Y_PASSWORD = "DyhtwjyfXqj6TRQk"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEED_TEST_URL = "https://www.speedtest.net/"

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        accept_button = WebDriverWait(driver=self.driver, timeout=10).until(
            ec.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        accept_button.click()
        time.sleep(3)
        
        go_button_click = self.driver.find_element(By.CSS_SELECTOR, value=".start-text a")
        go_button_click.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        print(self.down)

        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text
        print(self.up)

    def tweet_at_provider():
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

