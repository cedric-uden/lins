import ScreenInfo
import tkinter as tk
from GUI_Elements.Entries import MyEntry
from GUI_Elements.AskPath import AskPath
from GUI_Elements.ShowDisplayIndex import ShowDisplayIndex


class ConfiguratorGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configurator")
        self.enter_timer = MyEntry(self.root, focus=True, title="Enter Timer")
        self.enter_path = MyEntry(self.root, title="Enter the path")
        self.ask_path = AskPath(self.root)
        self.configure_root_window_dimensions()
        ShowDisplayIndex()
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
