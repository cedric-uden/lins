import tkinter as tk
from PIL import ImageTk
import threading as th


# --- functions ---
def on_click():
    load_image()
    t = th.Timer(5.0, load_image)
    t.start()


def load_image():
    global current_image_number

    current_image_number = (current_image_number+1) % len(images)
    # change image on canvas
    canvas.itemconfig(image_id, image=images[current_image_number])


# --- main ---
root = tk.Tk()

# canvas for image
canvas = tk.Canvas(root, width=60, height=60)
canvas.pack()

# button to change image
button = tk.Button(root, text="Change", command=on_click)
button.pack()

# images
images = [
    ImageTk.PhotoImage(file="images/1.jpg"),
    ImageTk.PhotoImage(file="images/2.jpg")
]
current_image_number = 0

# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=images[current_image_number])

root.mainloop()
