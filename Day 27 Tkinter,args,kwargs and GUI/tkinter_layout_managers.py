# pack(), place() and grid()
# Agar hum pack, place ya grid ka use nhi krte hai to wo cheez humari screen pr show nhi hogi
# Grid humari screens ko columns and rows mein tod deta hai
# **Important** Hum grid() ko agar use kr rhe hai kisi program mein to hum pack() ko nhi use
# kr skte uske sath and vice versa
# place() and pack() ka use hum aapas mein kr skte hai
# place() and grid() ka use bhi hum aapas mein kr skte hai

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # isse hume side-side se 20px chhodke hi saare labels, buttons and all show honge

my_label = tkinter.Label(text="This is old text")
my_label.config(text="This is new text")
# my_label.pack(side="right")
# my_label.place(x=0,y=0) # place use krne ka ek disadvantage ye hai ki isme hume bhut hi specific
                        # values deni hoti hai jo ki jb humare paas multiple cheeze hongi to difficult
                        # hoga ye krna 
my_label.grid(column=0,row=0)
my_label.config(padx=100, pady=100) #isse iss label ke charo taraf se 100px ki jagah bachi rhegi

button = tkinter.Button(text="Click Me")
# button.pack()
button.grid(column=1,row=1)

spindbox = tkinter.Spinbox(from_=0, to=10,width=5)
# spindbox.pack()
spindbox.grid(column=1, row=2)

window.mainloop()