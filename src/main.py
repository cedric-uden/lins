import time
import os
from PIL import ImageTk, Image
import FileSystemWatchdog
from Settings import Settings
from Window import Window

settings = Settings()

hot_folder_path = settings.path
image_extension = settings.extension

canvas_width = settings.canvas_width
canvas_height = settings.canvas_height
start_x = settings.start_x
start_y = settings.start_y

interval_between_images_in_seconds = 5

window = Window()


def load_all_image_paths():
    global all_images
    for path, dirs, files in os.walk(hot_folder_path):
        for filename in files:
            if filename[-len(image_extension):] == image_extension:
                all_images.add(hot_folder_path + filename)


def load_image():
    global window
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
    window.canvas.itemconfig(image_id, image=image)

    window.root.update()


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

image_id = window.create_canvas_and_get_id()
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
