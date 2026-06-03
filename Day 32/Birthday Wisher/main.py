import datetime
import pandas as pd
import random
import smtplib

my_email = "somitprogramming@gmail.com"
password = "csohdvmtpfnlcscr"

today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pd.read_csv("Day 32/Birthday Wisher/birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Day 32/Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday\n\n{content}"
            )
        


