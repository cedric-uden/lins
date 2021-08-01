import _tkinter
import time
import tkinter as tk
from PIL import ImageTk, Image


def load_image():
    global current_image_number
    global root

    current_image_number = (current_image_number+1) % len(images)
    # change image on canvas
    current_image = ImageTk.PhotoImage(images[current_image_number])
    canvas.itemconfig(image_id, image=current_image)
    root.update()


# --- main ---
root = tk.Tk()

w, h = 2560, 1400
start_x = 1920
start_y = 1120

root.overrideredirect(1)
root.geometry(f"%dx%d+{start_x}+{start_y}" % (w, h))
root.focus_set()
canvas = tk.Canvas(root, width=w, height=h)
canvas.pack()
canvas.configure(background='black')

# images
images = [
    Image.open("images/1.jpg"),
    Image.open("images/2.jpg"),
    Image.open("images/3.jpg")
]


# create canvas
image_id = canvas.create_image(0, 0, anchor='nw')
# and load the first image
current_image_number = -1
load_image()

ts = time.time()
while True:
    if time.time() - ts > 3:
        load_image()
        ts = time.time()

    try:
        pass
    except _tkinter.TclError:
        print("Window has been closed.")
        break
