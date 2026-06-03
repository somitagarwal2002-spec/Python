from tkinter import *

THEME_COLOR = "#375362"

class Quiz_interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Some Question Text", 
            fill=THEME_COLOR,
            font=("Arial",28,"italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_button_image = PhotoImage(file="Day 34/Quiz App/images/true.png")
        self.right_button = Button(image=right_button_image, highlightthickness=0)
        self.right_button.grid(row=2, column=0)

        wrong_button_image = PhotoImage(file="Day 34/Quiz App/images/false.png")
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)


        self.window.mainloop()




