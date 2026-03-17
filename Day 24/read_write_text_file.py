file = open("Day 24/my_file.txt")
contents = file.read()
print(contents)

file.close()



# file.close() likhna agr hum bhool bhi jaye to extra space na le humari file uske liye alag method

# agar humne kisi file ko khola aur wo file exist hi nhi krti to ye humare
# liye uss naam ki ek nayi file create kr deta hai

with open("Day 24/my_file.txt") as file:
    contents = file.read()
    print(contents)



# Agar hume apni file ko write krna ho to 

with open("Day 24/my_file.txt", mode="w") as file: # by default mode="r" read mein hota hai
    file.write("\nNew Text.")

# isse jo bhi pehle likha hoga wo saara hat jayega aur jo humne abhi likha hai keval whi rhega
# agar hum chahte hai ki purana wala rahe aur new bhi usse mein add ho jaye uske liye

with open("Day 24/my_file.txt", mode="a") as file: # mode="a" means appned
    file.write("\nNew Text.")


