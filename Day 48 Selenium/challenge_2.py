from selenium import webdriver
from selenium.webdriver.common.by import By

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name_fillup = driver.find_element(By.NAME, value="fName")
first_name_fillup.click()
first_name_fillup.send_keys("Somit")

last_name_fillup = driver.find_element(By.NAME, value="lName")
last_name_fillup.click()
last_name_fillup.send_keys("Agarwal")

email_fillup = driver.find_element(By.NAME, value="email")
email_fillup.click()
email_fillup.send_keys("my_email@gmail.com")

sign_up = driver.find_element(By.CLASS_NAME, value="btn-primary")
sign_up.click()
