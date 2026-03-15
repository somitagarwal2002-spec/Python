from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"

web = requests.get(URL)
print(web.status_code)

soup = BeautifulSoup(web.content, "html.parser")

whole = soup.select_one("span.a-price-whole").getText()
print(whole)
print(type(whole))

fraction = soup.select_one("span.a-price-fraction").getText()
print(fraction)
print(type(fraction))

full = float(whole + fraction)
print(full)
print(type(full))
