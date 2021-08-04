import ScreenInfo
import tkinter as tk


class ConfiguratorGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configurator")
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