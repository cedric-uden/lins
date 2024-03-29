import tkinter as tk
from src import ScreenInfo


class ShowDisplayIndex:

    def __init__(self):
        self.screens = ScreenInfo.ScreenInfo()
        self.bg_color = "#000"
        self.text_color = "#FFF"

        self.all_tk_roots = None
        self.all_tk_root_frames = None
        self.current_screen_index = None
        self.init_lists_and_index()

    def init_lists_and_index(self):
        self.current_screen_index = 0
        self.all_tk_roots = []
        self.all_tk_root_frames = []

    def build(self):
        for _ in self.screens.all_monitors:
            self.all_tk_roots.append(tk.Tk())
            current_root = self.all_tk_roots[self.current_screen_index]

            current_root.title(f"Window Picker {self.current_screen_index}")
            current_root.overrideredirect(1)
            current_root.configure(bg=self.bg_color)
            current_root.geometry(self.get_geometry())
            self.set_label()
            current_root.update()
            self.current_screen_index += 1

    def get_geometry(self):
        offset = 125
        start_x = self.screens.all_monitors[self.current_screen_index].x + offset
        start_y = self.screens.all_monitors[self.current_screen_index].y + offset
        return f"%dx%d+{start_x}+{start_y}" % (150, 100)

    def set_label(self):
        index_label = tk.Label(self.all_tk_roots[self.current_screen_index],
                               text=self.current_screen_index,
                               font=("Helvetica Neue", 72),
                               fg=self.text_color,
                               bg=self.bg_color,
                               )
        index_label.pack()

    def destruct_windows(self):
        for index in range(len(self.all_tk_roots)):
            self.all_tk_roots[index].destroy()
        self.init_lists_and_index()
