import tkinter as tk
import enum


class MyEntryOptions(enum.Enum):
    focus = "focus"


class MyEntry:

    def __init__(self, root, *args):
        self.root = root
        self.value = None
        self.frame = tk.Frame(self.root)
        self.frame.pack(anchor="nw")

        self.title_label = tk.Label(self.frame, text="Hello", anchor='w', width=10)
        self.title_label.pack(side=tk.LEFT)

        self.entry_payload = tk.Entry(self.frame, width=4)
        self.entry_payload.pack(side=tk.LEFT, padx=5)

        self.output_label = tk.Label(self.frame, text="")
        self.output_label.pack(side=tk.LEFT, padx=5)

        if MyEntryOptions.focus in args:  # focus the window with tab
            self.entry_payload.focus()
        self.entry_payload.bind("<Return>", self.return_entry)  # bind the return / enter key to action

        # Create and empty Label to put the result in
        self.output_label.pack(fill=tk.X)

    def return_entry(self, arg=None):
        """Gets the result from Entry and return it to the Label"""

        result = self.entry_payload.get()
        self.output_label.config(text=result)
        self.value = result
        self.entry_payload.delete(0, tk.END)
