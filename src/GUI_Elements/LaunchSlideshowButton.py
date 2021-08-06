import tkinter as tk
from src.RunLins import RunLins

# TODO: wip


class LaunchSlideshowButton:

    def __init__(self, root):
        self.root = root
        self.frame = None
        self.run_object = None
        self.button = None

        self.setup_frame()
        self.setup_button()

    def setup_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(anchor="nw")

    def run(self):
        self.run_object = RunLins()

    def setup_button(self):
        self.button = tk.Button(self.frame,
                                text="Launch Slideshow",
                                command=self.run,
                                )
        self.button.pack()
