import tkinter as tk
import enum


class MyEntryOptions(enum.Enum):
    focus = "focus"


class MyEntry:

    def __init__(self, root, *args):
        self.root = root
        self.value = None
        self.entry_payload = tk.Entry(self.root, width=4)
        self.title_label = tk.Label(self.root, text="Hello")
        self.output_label = tk.Label(self.root, text="")
        self.title_label.pack(fill=tk.X)

        # Create the Entry widget
        if MyEntryOptions.focus in args:
            self.entry_payload.focus()
        self.entry_payload.bind("<Return>", self.return_entry)
        self.entry_payload.pack()

        # Create and empty Label to put the result in
        self.output_label.pack(fill=tk.X)

    def return_entry(self, arg=None):
        """Gets the result from Entry and return it to the Label"""

        result = self.entry_payload.get()
        self.output_label.config(text=result)
        self.value = result
        self.entry_payload.delete(0, tk.END)
