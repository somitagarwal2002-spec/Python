from tkinter import *
from tkinter import messagebox # ye tkinter mein ek alag module hai isliye jb humne * 
                               # se saari classes call kr li fir bhi hume ise likhna 
                               # pad rha hai because messagebox is not a class it's a module
import random    
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    # isko change krke list comprehension ka use krke hum ise aur short form mein likhenge

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # instead of these three lines we can simply use joins in python 
    # Joins can be used to combine lists, tuples, dictinaries

    password = "".join(password_list) #"" hum space ya koi special character de skte hai like @ to jb hum list ke items ko add krenege to wo kuch aise aayenge like a aur b hai to a@b aayega
    print(f"Your password is: {password}")

    password_entry.insert(index="end", string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get() # jisse hum website_entry ki current value ko store kr sake
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:
                {
                    "email":email,
                    "password":password,
                }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="No Entry", message="Hey! You have left some fields empty")
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details \nEmail:{email}\nPassword:{password}\nIs it okay?")
        if is_ok:
            # data_file = open("Day 29/data.txt", "w")
            try:
                with open("Day 30/data.json", "r") as data_file: 
                
                # isse data_file.close() likhne ki zaroorat nhi
                
                # json.dump() used for writing in the file
                # json.dump(new_data, data_file, indent=4) 

                # json.load() used for reading json file
                    data = json.load(data_file) 
                # print(data)
            except FileNotFoundError:
                with open("Day 30/data.json","w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                # json.update() is used for updating json file
            else:
                data.update(new_data)

                with open("Day 30/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4) # here we are using json.dump() to wrtie new data in the new file
            finally: 
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        # data_file.close()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("Day 30/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password} ")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} Found")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus() # jb screen pop up hogi to cursor yha pr hoga

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(index="end", string="somit@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=11, command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)



window.mainloop()
