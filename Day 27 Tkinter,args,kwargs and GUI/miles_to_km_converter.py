import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=200, width=300)
window.config(padx=20, pady=20)

def calculate():
    given_miles = float(inputs.get())
    miles_to_km = given_miles * 1.609
    result_km.config(text=f"{miles_to_km}")

my_label = tkinter.Label(text="is equal to")
my_label.grid(column=0, row=1)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

inputs = tkinter.Entry(width=10)
mile = inputs.get()
inputs.grid(column=1, row=0)

result_km = tkinter.Label(text="0")
result_km.grid(column=1, row=1)

button = tkinter.Button(text="Calculate",command=calculate)
button.grid(column=1, row=2)

window.mainloop()
