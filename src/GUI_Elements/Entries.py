import tkinter as tk


class MyEntry:

    def __init__(self, root, **kwargs):
        self.root = root
        self.value = None
        self.frame = tk.Frame(self.root)
        self.frame.pack(anchor="nw")
        self.kwargs = kwargs

        self.title_label = tk.Label(self.frame, text=self.parse_title(), anchor='w', width=18)
        self.title_label.pack(side=tk.LEFT)

        self.entry_payload = self.create_and_get_entry_field()

        self.output_label = tk.Label(self.frame, text="")
        self.output_label.pack(side=tk.LEFT, padx=5)

        # Create and empty Label to put the result in
        self.output_label.pack(fill=tk.X)

    def create_and_get_entry_field(self):
        entry = tk.Entry(self.frame, width=4)
        entry.pack(side=tk.LEFT, padx=5)
        if "focus" in self.kwargs:
            if self.kwargs["focus"]:
                entry.focus()
        entry.bind("<Return>", self.return_entry)  # bind the return / enter key to action
        return entry

    def parse_title(self):
        if "title" in self.kwargs:
            return self.kwargs["title"]
        else:
            return "Title missing!"

    def return_entry(self, arg=None):
        """Gets the result from Entry and return it to the Label"""

        result = self.entry_payload.get()
        self.output_label.config(text=result)
        self.value = result
        self.entry_payload.delete(0, tk.END)
