import time
import FileSystemWatchdog
from Settings import Settings
from ImageHandler import ImageHandler


settings = Settings()
imh = ImageHandler()

hot_folder_path = settings.path

interval_between_images_in_seconds = 5

imh.load_all_image_paths()
imh.update_current_run_images()

my_obs = FileSystemWatchdog.MyObserver(hot_folder_path)
my_obs.start_observer()

imh.load_image()
ts = time.time()
print("Init Complete!")
while True:
    if time.time() - ts > interval_between_images_in_seconds:
        if my_obs.has_file_changes():
            new_images = my_obs.get_and_clean_file_changes_set()
            imh.new_images_not_yet_displayed.update(new_images)
            imh.all_images.update(new_images)

        if imh.counter_all_displayed_images == len(imh.all_images):
            imh.update_current_run_images()

        imh.load_image()
        ts = time.time()
