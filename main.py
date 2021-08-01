import time
import tkinter as tk
from PIL import ImageTk, Image

canvas_width = 2560
canvas_height = 1400
start_x = 1920
start_y = 1120


def load_image():
    global current_image_number
    global root

    current_image_number = (current_image_number+1) % len(images)

    pil_image = images[current_image_number]
    img_w, img_h = pil_image.size
    # resize photo to full screen
    ratio = min(canvas_width / img_w, canvas_height / img_h)
    img_w = int(img_w*ratio)
    img_h = int(img_h*ratio)
    pil_image = pil_image.resize((img_w, img_h), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pil_image)
    canvas.itemconfig(image_id, image=image)

    root.update()


# --- main ---
root = tk.Tk()

root.overrideredirect(1)
root.geometry(f"%dx%d+{start_x}+{start_y}" % (canvas_width, canvas_height))
root.focus_set()
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
canvas.configure(background='black')

# images
images = [
    Image.open("images/1.jpg"),
    Image.open("images/2.jpg"),
    Image.open("images/3.jpg")
]


# create canvas
image_id = canvas.create_image(canvas_width / 2,
                               canvas_height / 2,
                               anchor='center')
# and load the first image
current_image_number = -1
load_image()

ts = time.time()
while True:
    if time.time() - ts > 3:
        load_image()
        ts = time.time()
