import tkinter as tk
from Settings import Settings

settings = Settings()

canvas_width = settings.canvas_width
canvas_height = settings.canvas_height
start_x = settings.start_x
start_y = settings.start_y


class Window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(1)
        self.root.geometry(
            f"%dx%d+{start_x}+{start_y}" % (canvas_width, canvas_height))
        self.root.focus_set()

        self.canvas = tk.Canvas(self.root, width=canvas_width,
                                height=canvas_height)
        self.canvas.pack()
        self.canvas.configure(background='black')

    def create_canvas_and_get_id(self):
        image_id = self.canvas.create_image(canvas_width / 2,
                                            canvas_height / 2,
                                            anchor='center')
        return image_id
