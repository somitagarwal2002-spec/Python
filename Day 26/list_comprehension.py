# ****************************** List Comprehension ******************************
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# Ab iss 4 Line of code ko hum simply ek line mein likh skte hai 

# new_list = [new_item for item in list]  Syntax 

new_list =[n + 1 for n in numbers]
print(new_list)

# We can not only comprehend only lists (numbers here) we can also comprehend strings

name = "Somit"
# name_list = [letter for letter in name] Syntax 

name_list = [letter for letter in name]
print(name_list)



# ****************************** Python Sequences *******************************************

# List, Range, String, Tuple
# they are known as python seequences because they have particular order / sequence

# range(1,5)
range_list = [item * 2 for item in range(1,5)]
print(range_list)


# ****************************** Conditional List Comprehension ******************************

# new_list = [new_item for item in list if test] Syntax 

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_list  = [item for item in names if len(item)<= 4]
print(short_list)

upper_list = [item.upper() for item in names if len(item) > 5]
print(upper_list)


# ****************************** While Using Random Module ******************************

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for i in range(nr_letters)]
password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
