from datetime import datetime
import tkinter as tk
import time


class LogWindow:
    def __init__(self, main_window, width=700, height=400):
        self.width = width
        self.height = height

        self.window = tk.Toplevel(main_window)
        self.window.title('Log')
        self.window.geometry(f'{self.width}x{self.height}')
        self.window.resizable(width=False, height=False)

        scrollbar = tk.Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textArea = tk.Text(self.window, width=self.width,
                                height=self.height, yscrollcommand=scrollbar.set)
        self.textArea.pack(side=tk.TOP, fill=tk.X)

        self.lines = 0

    def insert_text(self, text):
        time = datetime.now().time()

        self.textArea.insert(f'{self.lines}.0', f'{time}: {text}\n')
        self.textArea.see('end')

        self.lines += 1

    def clear_text(self):
        self.textArea.delete('0.0', 'end')
