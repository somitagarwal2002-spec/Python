try:
    file = open("Day 30/a_file.txt")
    dictionary = {"key":"value"}
    a = dictionary["key"]
except FileNotFoundError: # ab ye dictionary wale error pr bhi dhyan de rha hai
    file = open("Day 30/a_file.txt", "w")
    file.write("Content of a_file")
except KeyError as error_message:
    print(f"This key {error_message} is not present")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("Error Raising")



# Calculating BMI

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height is less than 3 metres")

bmi = weight/height**2
print(round(bmi, 2))

