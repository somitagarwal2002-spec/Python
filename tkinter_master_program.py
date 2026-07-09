# Tkinter Master Program


"""
Covers:
- Tk window
- Label
- Button
- Entry
- Text
- Frame / LabelFrame
- Checkbutton
- Radiobutton
- Combobox
- Listbox
- Spinbox
- Scale
- Canvas
- Menu
- Messagebox
- filedialog
- Treeview
- Progressbar
- Notebook
- Event Binding
- Variables
- after()
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title("Tkinter Master Program")
root.geometry("900x650")

name = tk.StringVar()
agree = tk.BooleanVar()
gender = tk.StringVar(value="Male")

def submit():
    messagebox.showinfo("Data", f"Name: {name.get()}\nGender: {gender.get()}\nAgree: {agree.get()}")

def choose_file():
    path = filedialog.askopenfilename()
    if path:
        messagebox.showinfo("File", path)

def progress_run(v=0):
    if v <= 100:
        progress["value"] = v
        root.after(40, progress_run, v+5)

menu = tk.Menu(root)
fm = tk.Menu(menu, tearoff=0)
fm.add_command(label="Open", command=choose_file)
fm.add_command(label="Exit", command=root.destroy)
menu.add_cascade(label="File", menu=fm)
root.config(menu=menu)

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text="Widgets")
tabs.add(tab2, text="Treeview")

lf = ttk.LabelFrame(tab1, text="Demo")
lf.pack(fill="x", padx=10, pady=10)

ttk.Label(lf, text="Name").grid(row=0,column=0,padx=5,pady=5)
ttk.Entry(lf, textvariable=name).grid(row=0,column=1)

ttk.Radiobutton(lf,text="Male",variable=gender,value="Male").grid(row=1,column=0)
ttk.Radiobutton(lf,text="Female",variable=gender,value="Female").grid(row=1,column=1)

ttk.Checkbutton(lf,text="Accept",variable=agree).grid(row=2,column=0)

combo = ttk.Combobox(lf, values=["India","USA","UK"], state="readonly")
combo.current(0)
combo.grid(row=3,column=1)

spin = ttk.Spinbox(lf, from_=1, to=100)
spin.grid(row=4,column=1)

scale = ttk.Scale(lf, from_=0, to=100)
scale.grid(row=5,column=1, sticky="ew")

txt = tk.Text(lf,height=4,width=30)
txt.grid(row=6,column=0,columnspan=2)

lb = tk.Listbox(lf,height=4)
for i in ["Python","SQL","Excel","Power BI"]:
    lb.insert("end",i)
lb.grid(row=7,column=0)

canvas = tk.Canvas(lf,width=180,height=90,bg="white")
canvas.create_rectangle(10,10,70,60,fill="skyblue")
canvas.create_oval(90,10,160,70,fill="orange")
canvas.grid(row=7,column=1)

progress = ttk.Progressbar(lf,length=200)
progress.grid(row=8,column=0,columnspan=2,pady=10)

ttk.Button(lf,text="Submit",command=submit).grid(row=9,column=0)
ttk.Button(lf,text="Open File",command=choose_file).grid(row=9,column=1)
ttk.Button(lf,text="Progress",command=progress_run).grid(row=10,column=0,columnspan=2)

tree = ttk.Treeview(tab2, columns=("Name","Skill"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Skill", text="Skill")
tree.insert("", "end", values=("Somit","Python"))
tree.insert("", "end", values=("Amit","SQL"))
tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
