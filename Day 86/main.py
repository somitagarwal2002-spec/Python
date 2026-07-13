import tkinter as tk
from tkinter import messagebox
import random
import time
from paragraphs import PARAGRAPHS

HIGHSCORE_FILE = "Day 86/highscore.txt"

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("850x650")

        self.duration = 60
        self.time_left = self.duration
        self.running = False
        self.start_time = None

        self.sample_text = random.choice(PARAGRAPHS)

        tk.Label(root, text="Typing Speed Test", font=("Arial", 22, "bold")).pack(pady=10)

        self.sample = tk.Label(root, text=self.sample_text, wraplength=760,
                               justify="left", font=("Arial", 12), bg="black", padx=10, pady=10)
        self.sample.pack(fill="x", padx=20)

        self.timer_label = tk.Label(root, text="Time: 60", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        self.text = tk.Text(root, height=10, width=80, state="disabled")
        self.text.pack(pady=10)
        self.text.bind("<KeyPress>", self.first_key)

        btn = tk.Frame(root)
        btn.pack()

        tk.Button(btn, text="Start", width=15, command=self.start).grid(row=0, column=0, padx=10)
        tk.Button(btn, text="Restart", width=15, command=self.restart).grid(row=0, column=1, padx=10)

        self.result = tk.Label(root, font=("Arial", 12), justify="left")
        self.result.pack(pady=20)

        self.highscore = self.load_highscore()
        self.update_result(0,0,0,0)

    def load_highscore(self):
        try:
            with open(HIGHSCORE_FILE,"r") as f:
                return int(f.read().strip() or 0)
        except:
            return 0

    def save_highscore(self, wpm):
        if wpm > self.highscore:
            self.highscore = wpm
            with open(HIGHSCORE_FILE,"w") as f:
                f.write(str(wpm))

    def update_result(self,wpm,acc,corr,wrong):
        self.result.config(text=f"WPM: {wpm}\nAccuracy: {acc:.2f}%\nCorrect Words: {corr}\nWrong Words: {wrong}\nHigh Score: {self.highscore}")

    def start(self):
        if self.running:
            return
        self.running=True
        self.time_left=self.duration
        self.text.config(state="normal")
        self.text.delete("1.0","end")
        self.text.focus()
        self.start_time=None
        self.countdown()

    def first_key(self,event):
        if self.running and self.start_time is None:
            self.start_time=time.time()

    def countdown(self):
        self.timer_label.config(text=f"Time: {self.time_left}")
        if self.running and self.time_left>0:
            self.time_left-=1
            self.root.after(1000,self.countdown)
        elif self.running:
            self.finish()

    def finish(self):
        self.running=False
        self.text.config(state="disabled")
        typed=self.text.get("1.0","end").strip()
        sample_words=self.sample_text.split()
        typed_words=typed.split()

        correct=sum(1 for a,b in zip(sample_words,typed_words) if a==b)
        wrong=max(len(typed_words)-correct,0)
        total=max(len(typed_words),1)
        acc=(correct/total)*100
        elapsed=self.duration/60
        wpm=round(len(typed_words)/elapsed)
        self.save_highscore(wpm)
        self.update_result(wpm,acc,correct,wrong)
        messagebox.showinfo("Finished",f"Your WPM: {wpm}")

    def restart(self):
        self.running=False
        self.sample_text=random.choice(PARAGRAPHS)
        self.sample.config(text=self.sample_text)
        self.timer_label.config(text="Time: 60")
        self.text.config(state="normal")
        self.text.delete("1.0","end")
        self.text.config(state="disabled")
        self.update_result(0,0,0,0)

root=tk.Tk()
TypingSpeedTest(root)
root.mainloop()
