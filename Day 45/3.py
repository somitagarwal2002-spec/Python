# Extracting Text which is preseent inside a tag

import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/")

soup = BeautifulSoup(web.content, "html.parser")

lines = soup.find_all("p")
print(lines) # ye hrr paragraph ko nikal ke dega in a list format

for l in lines:
    print(l.text) # isse keval text jo likha hoga wo scrape hoga aur uske alawa kuch nhi, naa hi class, naa hi id

s = soup.find("div", class_="why-choose-card card-shadow card")
print(s)

lines_1 = s.find_all("p")
print(lines_1)

for l1 in lines_1:
    print(l1.text)

# hum div ka naa use krke keval uss paragraph aur class ka use krke bhi simply apna kaam aram se kr skte the

s1 = soup.find("p", class_= "fs-16 fw-400 lh-24 label-color-1 card-text")
print(s1.text)

