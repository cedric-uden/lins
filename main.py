import time
import tkinter as tk
from PIL import ImageTk


def load_image(current_root):
    global current_image_number

    current_image_number = (current_image_number+1) % len(images)
    # change image on canvas
    canvas.itemconfig(image_id, image=images[current_image_number])
    current_root.update()


# --- main ---
root = tk.Tk()

# canvas for image
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# images
images = [
    ImageTk.PhotoImage(file="images/1.jpg"),
    ImageTk.PhotoImage(file="images/2.jpg")
]
current_image_number = 0

# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=images[current_image_number])

while True:
    load_image(root)
    time.sleep(3)
