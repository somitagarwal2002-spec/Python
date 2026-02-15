# Web scraping Basics

import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/")

print(web.status_code)

print(web.content) # this will print all the html code of the website in a paragraph format

soup = BeautifulSoup(web.content, "html.parser")

print(soup.prettify()) # ye humare html code ko html tree mein ache se show krega

print(soup.title) # tab mein jo naam likha hota hai wo isse likh ke aa jayega, it includes title tag too i.e <title>

print(soup.p) # first jo paragraph tag aayega wo show hoga with <p> tag

print(soup.a) # first anchor tag aayega wo show hoga with <a> tag

print(soup.h1) # first header 1 tag will be shown with <h1> tag





# ************************ Navigable String ********************************************

# hrr tag ke andar jo content likha hoga use keval extract krne ke liye hum inka use krte hai
# aur agr kuch nhi likha hoga to None return krega

print(soup.p.string) # first paragraph tag ke content ko show krega keval

print(soup.a.string) # first anchor tag ke content ko show krega keval 

print(soup.h1.string) # first heading 1 tag ke content ko show krega keval




# ************************ Beautiful Soup ********************************************

# hume apni website se kisi bhi data ko fetch krne ke liye iska use hota hai

print(soup.title) # tab mein jo naam likha hota hai wo isse likh ke aa jayega, it includes title tag too i.e <title>

print(soup.p) # first jo paragraph tag aayega wo show hoga with <p> tag

print(soup.a) # first anchor tag aayega wo show hoga with <a> tag

print(soup.h1) # first header 1 tag will be shown with <h1> tag

# ** functions in Beautiful Soup **

print(soup.find("h1")) # ye sabse pehle h1 tag ko find krega

print(soup.find_all("p")) # ye saare p tag ko find krke output dega



# ************************ Comments ********************************************
# agr humare html code mein khi bhi comment likhe honge to unhe extract krne ke liye hum comments ka use krte hai




