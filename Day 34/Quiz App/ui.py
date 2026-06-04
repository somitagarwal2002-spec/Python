from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
INITIAL = 0

class Quiz_interface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {INITIAL}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some Question Text", 
            fill=THEME_COLOR,
            font=("Arial",28,"italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_button_image = PhotoImage(file="Day 34/Quiz App/images/true.png")
        self.right_button = Button(image=right_button_image, highlightthickness=0, command=self.right_button_clicked)
        self.right_button.grid(row=2, column=0)

        wrong_button_image = PhotoImage(file="Day 34/Quiz App/images/false.png")
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=self.wrong_button_clicked)
        self.wrong_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_button_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)






