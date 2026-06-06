from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# jo special keys hoti hai keyboard ki jaise tab, shift, enter, etc. unhe press krne ke liye hum iss library ko import kiya hai

# to keep browser open after program finishes follow this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a')
print(article_count.text)

# used to click on a link or something which is clickable
article_count.click()


# By.LINK_TEXT specifically aisi hi link ke text ko directly use krne ke liye hota hai
ipl = driver.find_element(By.LINK_TEXT, value="Indian Premier League")
ipl.click()


# kisi search box mein type krne ke liye
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
