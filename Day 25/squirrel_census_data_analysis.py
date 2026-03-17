import pandas as pd

data = pd.read_csv("Day 25/squirrel_dataset.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
print(gray)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon)
black = len(data[data["Primary Fur Color"] == "Black"])
print(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"], 
    "Count" : [gray, cinnamon, black]
}

print(data_dict)

df = pd.DataFrame(data_dict)
df.to_csv("Day 25/squirrel_color_count.csv")


