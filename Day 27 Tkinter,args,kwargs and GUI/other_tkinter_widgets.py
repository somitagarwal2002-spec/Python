import tkinter

window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Label, Button, Text, Entry, Spinbox, Scale, Radio Button, Check button, List box

my_label = tkinter.Label(text="This is old text")
my_label.config(text="This is new text")
my_label.pack()

def action():
    print("Do Something")

button = tkinter.Button(text="Click Me",command=action)
button.pack()

inputs = tkinter.Entry(width=30)
inputs.insert(index="end",string="Some text to begin with")
print(inputs.get())
inputs.pack()

text = tkinter.Text(height=5, width=30)
text.focus() # isse humara cursor yha pr rhega initailly
text.insert(index="end",chars="Example of a multilinetext to entry")
print(text.get("1.0")) # starting from 1st line at character 0
text.pack()

def spinbox_used():
    print(spindbox.get())

spindbox = tkinter.Spinbox(from_=0, to=10,width=5, command=spinbox_used)
spindbox.pack()



def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100,command=scale_used)
scale.pack()


def checkbutton_used():
    print(checked_state.get())
checked_state = tkinter.IntVar() # ye intvar() 0 aur 1 ke beech number mein se chose krega
checkbutton = tkinter.Checkbutton(text="Is ON?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox()
fruits = ["apple", "pear", "banana", "orange"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()



window.mainloop()