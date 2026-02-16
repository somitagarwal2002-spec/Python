# Scrapping Links and Image Information in web page

import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/")

soup = BeautifulSoup(web.content, "html.parser")

soup.prettify()

# ******************************** Scrapping Links ***********************************************************

for i in soup.find_all("a"):
    print(i.get("href"))


# **************************** Scrapping Image &Image Information ***************************************************

# image url is present in src 
img = soup.find_all("img")

print(img)

for i in img:
    print(i.get("src"))



