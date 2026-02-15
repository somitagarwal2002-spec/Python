import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/")

print(web.status_code)

# print(web.content) # this will print all the html code of the website in a paragraph format

soup = BeautifulSoup(web.content, "html.parser")

# print(soup.find_all("p"))

# ************************** Finding Elements By Class *******************************************

class_data = soup.find("div",class_ = "compiler-icon-wrapper mb-0 me-3 rounded-circle d-flex align-items-center justify-content-center")
# print(class_data)

# particular <div> tag mein jiss class ka naam hoga ye uss div tag ki saari information aa jayegi
# including <div> tag

print(class_data.find_all("span")) 
# jo div tag nikala hai usme jitne 




# ************************** Finding Elements By Class *******************************************
# yhi saara kaam jo humne class ki help se kiya hai whi hum id ki help se bhi kr skte hai

id_data = soup.find("div", id= "svg-inline--fa-title-Mcmpl3E3NN2X")
print(id_data.find_all("p"))






