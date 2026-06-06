import smtplib
import datetime as dt

my_email = "my_email"
password = "my_password"

dob = dt.datetime(year=2002, month=8, day=3)
now = dt.datetime.now()

if now.day==3 and now.month==8 and now.year==2026:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sumitjaiswal4844@gmail.com",
            msg="Subjext:Birthday Wish\n\nHappy Birthday to You❤️✨🥂"
        )

