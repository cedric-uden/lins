import tkinter as tk
from src import ScreenInfo


class ShowDisplayIndex:

    def __init__(self):
        self.screens = ScreenInfo.ScreenInfo()
        self.all_tk_roots = []
        self.all_tk_root_frames = []

        self.current_screen_index = 0
        self.for_all_screens()

    def for_all_screens(self):
        for _ in self.screens.all_monitors:
            self.all_tk_roots.append(tk.Tk())
            current_root = self.all_tk_roots[self.current_screen_index]

            current_root.overrideredirect(1)
            # current_root.configure(background="black")
            current_root.geometry(self.get_geometry())
            self.set_label()
            current_root.update()
            self.current_screen_index += 1

    def get_geometry(self):
        offset = 125
        start_x = self.screens.all_monitors[self.current_screen_index].x + offset
        start_y = self.screens.all_monitors[self.current_screen_index].y + offset
        return f"%dx%d+{start_x}+{start_y}" % (150, 150)

    def set_label(self):
        index_label = tk.Label(self.all_tk_roots[self.current_screen_index],
                               text=self.current_screen_index
                               )
        index_label.pack()

