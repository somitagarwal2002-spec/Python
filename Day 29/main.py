from tkinter import *
from tkinter import messagebox # ye tkinter mein ek alag module hai isliye jb humne * 
                               # se saari classes call kr li fir bhi hume ise likhna 
                               # pad rha hai because messagebox is not a class it's a module
import random    
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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="No Entry", message="Hey! You have left some fields empty")
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details \nEmail:{email}\nPassword:{password}\nIs it okay?")
        if is_ok:
            # data_file = open("Day 29/data.txt", "a")
            with open("Day 29/data.txt", "a") as data_file: 
                # isse data_file.close() likhne ki zaroorat nhi
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        # data_file.close()

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
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



window.mainloop()
