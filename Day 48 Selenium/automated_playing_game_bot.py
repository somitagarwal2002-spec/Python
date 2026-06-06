# More To Do 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

condition = True
check_5_second = time.time() + 5

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

language_selector = WebDriverWait(driver=driver, timeout=10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="langSelect-EN"]')
    )
)

language_selector.click()

time.sleep(2)

cookie_clicker = WebDriverWait(driver=driver, timeout=10).until(
    EC.element_to_be_clickable(
        (By.ID, "bigCookie")
    )
)

# cookie_clicker.click()
# cookie_clicker.click()
# cookie_clicker.click()
# cookie_clicker.click()
# cookie_clicker.click()

time.sleep(2)

count_cookie_click = driver.find_element(By.CSS_SELECTOR, value="div#cookies.title")
count = int(count_cookie_click.text.split(" ")[0])
# print(type(count))

# while condition:
#     cookie_clicker.click()
