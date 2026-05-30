import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(now)
print(type(now))
print(year)
print(type(year))
print(month)
print(day_of_week)

dob = dt.datetime(year=2002 , month=11 , day=13)
print(dob)
