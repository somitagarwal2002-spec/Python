from selenium import webdriver
# webdriver hi humara saara kaam krne wala hai jo bhi hum chrome pe krne wale hai
from selenium.webdriver.common.by import By

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")
driver.get("https://www.python.org/")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The Price is {price_dollar.text}.{price_cents.text}")


# for python org website 
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link_using_css = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link_using_css.text)

# Agar upr diye hue saare methods fail ho jaye ya fir kaam na kare to iss method ko use krna 👇
using_xpath = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(using_xpath.text)



driver.close() # it closes the particular active tab
driver.quit() # it closes the entire browser
# It totally depends upon you 👆

