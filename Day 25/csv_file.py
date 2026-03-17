with open("Day 25/weather_data.csv") as datafile:
    data = datafile.readlines()
    print(data)

#  isme dikkat ye aa rhi thi ki humare list ke ek hi item mein comma separated kayi sari values
# thi jise clean krna aur tough kr deta isliye import csv method use kiya hai



import csv

with open("Day 25/weather_data.csv") as datafile:
    data = csv.reader(datafile)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)



# Pandas se ye saare kaam aur asaan ho jate hai

import pandas as pd

data = pd.read_csv("Day 25/weather_data.csv")
print(data)
print(data["temp"])

