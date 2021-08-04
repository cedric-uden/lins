import ScreenInfo
import tkinter as tk
from GUI_Elements.Entries import MyEntry, MyEntryOptions


class ConfiguratorGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configurator")
        self.enter_timer = MyEntry(self.root, MyEntryOptions.focus)
        self.enter_path = MyEntry(self.root)
        self.configure_root_window_dimensions()
        self.root.mainloop()

    def configure_root_window_dimensions(self):
        width_percentage = 50
        height_percentage = 60
        primary = ScreenInfo.ScreenInfo().get_primary()
        self.root.configure(
            width=(width_percentage / 100) * primary.width,
            height=(height_percentage / 100) * primary.height,
        )
        target_width = int((width_percentage / 100) * primary.width)
        target_height = int((height_percentage / 100) * primary.height)
        start_x = int(((1 - (width_percentage / 100)) / 2) * primary.width)
        start_y = int(((1 - (height_percentage / 100)) / 2) * primary.height)
        geometry = f"%dx%d+{start_x}+{start_y}" % (target_width, target_height)
        self.root.geometry(geometry)
