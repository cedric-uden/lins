import _tkinter
import time
import tkinter as tk
from PIL import ImageTk


def load_image(current_root):
    global current_image_number

    current_image_number = (current_image_number+1) % len(images)
    # change image on canvas
    current_image = get_tk_photo_image(current_image_number)
    canvas.itemconfig(image_id, image=current_image)
    current_root.update()


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
    ImageTk.PhotoImage(file="images/1.jpg"),
    ImageTk.PhotoImage(file="images/2.jpg")
]


def get_tk_photo_image(index):
    return images[index]


# create canvas
image_id = canvas.create_image(0, 0, anchor='nw')
# and load the first image
current_image_number = -1
load_image(root)

ts = time.time()
while True:
    if time.time() - ts > 3:
        load_image(root)
        ts = time.time()

    try:
        root.update()
    except _tkinter.TclError:
        print("Window has been closed.")
        break
