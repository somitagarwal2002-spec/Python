from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://appbrewery.github.io/instant_pot/"
MY_EMAIL = "my_email"
PASSWORD = "my_password"

headers = {
    "User-Agent":"my_user_agent",
    "Accept-Language":"en-US"
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
soup.prettify()

whole = soup.select_one("span.a-price-whole").getText()
print(whole)
print(type(whole))

fraction = soup.select_one("span.a-price-fraction").getText()
print(fraction)
print(type(fraction))

final_price = float(whole + fraction)
print(final_price)
print(type(final_price))

if final_price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="somitagarwal2002@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\nInstant Pot price is less than $100\nBuy Now!!!!!"
        )


