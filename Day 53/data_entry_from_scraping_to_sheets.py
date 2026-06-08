from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdAhL0nnw3Uvn8UazME27yRS8s3hFWoToQ4oQuaUzXtopozYA/viewform?usp=publish-editor'
ZILLOW_WEBSITE_URL = 'https://appbrewery.github.io/Zillow-Clone/'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=ZILLOW_WEBSITE_URL, headers=headers)
print(response.status_code)
response.raise_for_status()

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
soup.prettify()

scraping_address = soup.select(".StyledPropertyCardDataWrapper address")
# print(scraping_address)
all_addresses = [address.get_text().strip() for address in scraping_address]
# print(len(all_addresses))
# print(all_addresses[0])

scrapping_price = soup.select(".PropertyCardWrapper .PropertyCardWrapper__StyledPriceLine")
# print(scrapping_price)
all_prices = [price.get_text().replace("/mo"," ").split("+")[0].strip() for price in scrapping_price]
# print(len(all_prices))
# print(all_prices[0])

scrapping_links = soup.select(".StyledPropertyCardDataArea-anchor")
all_links = [link["href"] for link in scrapping_links]
# print(len(all_links))
# print(all_links[0])

# Now we have 3 lists all_addresses, all_prices and all_links jiske andar humara saara required data hai

# Selenium Part (Form Filling)

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(all_links)):
    time.sleep(1)
    driver.get(FORM_URL)

    time.sleep(3)

    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(all_addresses[i])

    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(all_prices[i])

    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[i])

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()


