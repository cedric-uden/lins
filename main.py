import time
import os
import tkinter as tk
from PIL import ImageTk, Image
import FileSystemWatchdog
import Settings


settings = Settings.Linux

hot_folder_path = settings.path
image_extension = settings.extension

canvas_width = settings.canvas_width
canvas_height = settings.canvas_height
start_x = settings.start_x
start_y = settings.start_y

interval_between_images_in_seconds = 5


def load_all_image_paths():
    global all_images
    for path, dirs, files in os.walk(hot_folder_path):
        for filename in files:
            if filename[-len(image_extension):] == image_extension:
                all_images.add(hot_folder_path + filename)


def load_image():
    global root
    global new_images_not_yet_displayed
    global current_run_images
    global new_images_not_yet_displayed
    global counter_all_displayed_images

    if len(new_images_not_yet_displayed) > 0:
        pil_image = Image.open(new_images_not_yet_displayed.pop())
    else:
        pil_image = Image.open(current_run_images.pop())

    counter_all_displayed_images += 1

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


def update_current_run_images():
    global all_images
    global current_run_images
    global counter_all_displayed_images
    current_run_images = set()
    current_run_images.update(all_images)
    counter_all_displayed_images = 0


# images
counter_all_displayed_images = 0

all_images = set()
load_all_image_paths()

current_run_images = set()
update_current_run_images()

new_images = set()
new_images_not_yet_displayed = set()

# create canvas
image_id = canvas.create_image(canvas_width / 2,
                               canvas_height / 2,
                               anchor='center')
# and load the first image
load_image()

my_obs = FileSystemWatchdog.MyObserver(hot_folder_path)
my_obs.start_observer()

ts = time.time()
print("Init Complete!")
while True:
    if time.time() - ts > interval_between_images_in_seconds:
        if my_obs.has_file_changes():
            new_images = my_obs.get_and_clean_file_changes_set()
            new_images_not_yet_displayed.update(new_images)
            all_images.update(new_images)

        if counter_all_displayed_images == len(all_images):
            update_current_run_images()

        load_image()
        ts = time.time()
