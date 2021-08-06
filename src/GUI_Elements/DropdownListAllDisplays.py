import tkinter as tk

# TODO: wip


class DropdownListAllDisplays:

    def __init__(self, root):
        self.root = root
        self.frame = None
        self.menu = None

        self.setup_frame()
        self.setup_dropdown()

    def setup_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(anchor="nw")

    def setup_dropdown(self):
        self.menu = tk.Menu(self.frame)
        self.menu.add_cascade()
        # self.menu.pack()
