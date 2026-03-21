import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))
my_label.pack()  # jo bhi my_label mein likha hai wo center mein show hoga in top area
                 # agr hum .pack() ko nhi use krte hai to Label hume screen pr show hi nhi hoga
# my_label.pack(side="left") #ye left side mein center mein jayega (-500, 0)
# my_label.pack(expand=True) # ye ekdum middle of the page/layout pr aayega

# Buttons

def button_clicked():
    print("I got Clicked")
    my_label.config(text="Button got Clicked")
    # OR
    my_label["text"] = "Button got Clicked"

button = tkinter.Button(text="Click Me",command=button_clicked)
button.pack()

# Entry

inputs = tkinter.Entry(width=10)
inputs.pack()
print(inputs.get())

def button_clicked():
    print("I got Clicked")
    my_label.config(text=inputs.get())
    # OR
    # my_label["text"] = "Button got Clicked"

button = tkinter.Button(text="Click Me",command=button_clicked)
button.pack()


# *args : Many Positional Arguments

def add(*numbers): #zaroori nhi ki *args hi likhe kuch bhi likh sakte hai
    print(numbers[0]) # 1
    print(numbers[2]) # 3
    print(type(numbers))
    sum = 0
    for n in numbers: # we can give as many arguments we want, they will be stored in form of tuple
        sum += n
    print(sum)

add(1,2,3,4,5)

def calculate(n, **kwargs): # kwargs = key word arguments
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# Creating a class with key word arguments

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="nissan")
print(my_car.make)
print(my_car.model)

window.mainloop()
