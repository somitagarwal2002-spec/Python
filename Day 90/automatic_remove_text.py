import tkinter as tk

TIMEOUT = 5000  # 5 seconds


class AutomaticRemoveText:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("900x600")

        self.timer_id = None

        self.info = tk.Label(
            root,
            text="Keep typing! If you stop for 5 seconds, everything will be deleted.",
            font=("Arial", 12),
        )
        self.info.pack(pady=10)

        self.text = tk.Text(root, wrap="word", font=("Arial", 14))
        self.text.pack(expand=True, fill="both", padx=15, pady=10)
        self.text.focus()

        self.text.bind("<Key>", self.reset_timer)

        self.start_timer()

    def start_timer(self):
        self.timer_id = self.root.after(TIMEOUT, self.clear_text)

    def reset_timer(self, event=None):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.start_timer()

    def clear_text(self):
        self.text.delete("1.0", tk.END)
        self.info.config(
            text="You stopped typing for 5 seconds. Your work was deleted!"
        )
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    AutomaticRemoveText(root)
    root.mainloop()
