from tkinter.filedialog import askdirectory
import tkinter as tk
from src import Settings


class AskPath:

    def __init__(self, root):
        self.root = root
        self.settings = Settings.Settings()

        self.last_valid_path = self.settings.path
        self.get_path = self.last_valid_path
        self.frame_label = None
        self.frame_button = None
        self.button = None
        self.path_label = None

        self.build_frame()

    def build_frame(self):
        self.setup_frame()
        self.setup_label()
        self.setup_current_selected_path_label()
        self.path_button()

    def setup_label(self):
        title_label = tk.Label(self.frame_label,
                               text="Current path: ",
                               anchor='w',
                               width=18,
                               )
        title_label.pack(side=tk.LEFT)

    def setup_current_selected_path_label(self):
        self.path_label = tk.Label(self.frame_label,
                                   text=self.get_path,
                                   )
        self.path_label.pack(side=tk.LEFT)

    def setup_frame(self):
        self.frame_label = tk.Frame(self.root)
        self.frame_label.pack(anchor="nw")
        self.frame_button = tk.Frame(self.root)
        self.frame_button.pack(anchor="nw")

    def path_button(self):
        self.button = tk.Button(self.frame_button,
                                text="Choose a different path",
                                command=self.ask_dir)
        self.button.pack(anchor="nw", padx=163)

    def ask_dir(self):
        self.get_path = askdirectory()
        if self.path_entered_successfully():
            self.updated_validated_path()

    def path_entered_successfully(self):
        return self.get_path != ""

    def updated_validated_path(self):
        self.last_valid_path = self.get_path
        self.path_label.config(text=self.last_valid_path)
