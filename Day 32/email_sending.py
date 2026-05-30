import smtplib

my_email = "somitprogramming@gmail.com"
password = "csohdvmtpfnlcscr"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="sumitjaiswal4844@gmail.com", 
        msg="Subject:Test\n\nHello"
        )

# connection.close() ise hume tb likhna hota jb humne with ke sath nhi likha hota connection ko

