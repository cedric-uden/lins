import tkinter as tk
from .ShowDisplayIndex import ShowDisplayIndex


init_text = "Show Display Indices"
close_text = "Hide Display Indices"


class ShowDisplayIndexButton:

    def __init__(self, root):
        self.root = root
        self.frame = None
        self.build_button = None
        self.show_display_index_call = ShowDisplayIndex()
        self.is_displaying = False

        self.init_frame()
        self.build_display_button()

    def init_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(anchor="nw")

    def build_display_button(self):
        self.build_button = tk.Button(self.frame,
                                      text=init_text,
                                      command=self.show_display_index,
                                      )
        self.build_button.pack()

    def show_display_index(self):
        if self.is_displaying:
            self.show_display_index_call.destruct_windows()
        else:
            self.show_display_index_call.build()
        self.update_status_message()
        self.toggle_state()

    def toggle_state(self):
        self.is_displaying = not self.is_displaying

    def update_status_message(self):
        if self.is_displaying:
            self.build_button.config(text=init_text)
        else:
            self.build_button.config(text=close_text)
