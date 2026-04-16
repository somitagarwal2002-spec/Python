# # FileNotFound Error
with open("a_file.txt") as file:
    file.read()

# # KeyError
dictionary = {"key":"value"}
a = dictionary["b"]

# # IndexError or Index out of range
a = [1, 2, 3]
print(a[4])

# # TypeError
text = "abc"
print(text + 5)


# *********************************** Handling Exceptions *************************************************

# These 4 keywords are really important for handling error or exceptions

# try: something that might cause exception
# except:do this if there was an exception 
# else: do this if there were no exceptions and after try get executed and there are no exceptions in try block
# finally: do this no matter what happens

# Catching FileNotFound Error/Exception
try:
    file = open("Day 30/a_file.txt")
    dictionary = {"key":"value"}
    a = dictionary["b"]
except:
    file = open("Day 30/a_file.txt", "w") # "w"(write) mode mein open krne se agar ye file nhi hogi to ye uss file ko bana dega
    file.write("Content of a_file")
# humne except mein error ko define nhi kiya isliye jb hum dictionary mein error de rhe hai fir bhi except block use eroor nhi treat kr rha hai

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
    print("This will run no matter what")
    file.close()
