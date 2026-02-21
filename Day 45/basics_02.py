from bs4 import BeautifulSoup
import lxml

with open("file_name.html") as file: # ye line hum use kr rhe hai taki iss naam ki file humare system mein ho use open karne ke liye
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") # lxml ke liye html.parser ki jagah lxml bss likhna hoga

company_url = soup.select_one(selector="p a") # aisa anchor tag do jo ek paragraph tag ke andar ho and it will give first matching item

company = soup.select(selector="p a") # ye saare anchor tag dega jo paragraph tag ke andar honge

# select_one ka use keval ek ko select krne ke liye hota hai wo bhi jo first occuring ho
# select ka use saari cheeze ko select krne ke liye hota hai in the program

company_url = soup.select_one(selector="#main") # jis bhi tag ki id main hogi wo select hoga

company = soup.select(selector=".heading") # jin bhi tags ki class heading hongi ye sbko print krega

