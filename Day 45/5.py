# Scraping IPL teams Top Buys

import requests
from bs4 import BeautifulSoup
import pandas as pd

web = requests.get("https://www.iplt20.com/auction")

soup = BeautifulSoup(web.content, "html.parser")

soup.prettify()

table = soup.find("table", class_ = "ih-td-tab w-100 auction-tbl")

title = table.find_all("th")

headers = []
for i in title:
    name = i.text.strip()  # .strip() add kiya extra spaces hatane ke liye
    headers.append(name)

print("Headers:", headers)  # Check karo ki kitne columns hain

df = pd.DataFrame(columns=headers)
print(df)

rows = table.find_all("tr")

for i in rows[1:]:
    try:
        # First column ka data
        first_td = i.find_all("td")[0].find("div", class_ = "ih-pt-ic")
        if first_td:
            first_data = first_td.text.strip()
        else:
            first_data = i.find_all("td")[0].text.strip()  # Agar div nahi mila toh td ka text lo
        
        # Baaki columns ka data
        data = i.find_all("td")[1:]
        row = [tr.text.strip() for tr in data]  # .strip() add kiya
        
        # First column add karo
        row.insert(0, first_data)
        
        print(f"Row length: {len(row)}, Headers length: {len(headers)}")  # Debug ke liye
        print(f"Row data: {row}")  # Ye dekho ki data sahi aa raha hai
        
        # Check karo ki row aur headers ki length match karti hai
        if len(row) == len(headers):
            l = len(df)
            df.loc[l] = row
        else:
            print(f"Skipping row - length mismatch: {row}")
            
    except Exception as e:
        print(f"Error in row: {e}")
        continue

print("\nFinal DataFrame:")
print(df)

# CSV mein save karo
df.to_csv("ipl_auction_data.csv", index=False)
print("\nData saved to ipl_auction_data.csv")

