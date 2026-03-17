import pandas as pd

data = pd.read_csv("Day 25/weather_data.csv")

print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Calculating Average of temp_list
count = 0
for tem in range(0, len(temp_list)):
    count += temp_list[tem]

print(count/len(temp_list))

# Alternate method of calculating average of temp_list
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

# Most Optimal Method using Pandas
avg = data["temp"].mean()
print(avg)

# Maximum Value in temp_list
print(data["temp"].max())

# Method for calling a particular column
print(data["condition"]) # here "condition" is known as key
# OR
print(data.condition) # here "condition" is known as attribute
# Hum dono mein se koi bhi chose kr skte hai



# Getting data of a row
print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])


monday = data[data.day == "Monday"]
print(monday.temp)

celsius = monday.temp
fahrenheit = (9*celsius)/5 + 32
print(fahrenheit)

print((9 * monday.temp)/5 + 32)




# Creating a dataframe from scratch

dic = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

df_data = pd.DataFrame(dic)
print(df_data)
df_data.to_csv("Day 25/new_data.csv")
