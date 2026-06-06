import datetime as dt
import smtplib
import random

today = dt.datetime.now()
day_of_today = today.weekday()

if day_of_today == 5:
    with open("Day 32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    my_email = "my_email"
    password = "my_password"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="somitagarwal2002@gmail.com", 
            msg=f"Subject:Today's Quote\n\n{quote}"
        )


