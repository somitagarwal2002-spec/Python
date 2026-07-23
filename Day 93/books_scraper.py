import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL="https://books.toscrape.com/catalogue/page-{}.html"

data=[]

for page in range(1,6):
    print(f"Scraping page {page}...")
    r=requests.get(BASE_URL.format(page),timeout=30)
    soup=BeautifulSoup(r.text,"html.parser")

    books=soup.select("article.product_pod")

    for book in books:
        title=book.h3.a["title"]
        price=book.select_one(".price_color").get_text(strip=True)
        availability=book.select_one(".availability").get_text(strip=True)
        rating=book.p["class"][1]

        data.append({
            "Title":title,
            "Price":price,
            "Availability":availability,
            "Rating":rating
        })

df=pd.DataFrame(data)
df.to_csv("Day 93/books.csv",index=False,encoding="utf-8-sig")

print(f"Saved {len(df)} books to books.csv")
