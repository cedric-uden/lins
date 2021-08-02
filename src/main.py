import time
import FileSystemWatchdog
from Settings import Settings
from ImageHandler import ImageHandler


settings = Settings()
imh = ImageHandler()

hot_folder_path = settings.path
interval_between_images_in_seconds = settings.interval_between_images_in_seconds

imh.load_all_image_paths()
imh.update_current_run_images()

my_obs = FileSystemWatchdog.MyObserver(hot_folder_path)
my_obs.start_observer()


def load_new_images(observer, image_handler):
    new_images = observer.get_and_clean_file_changes_set()
    image_handler.new_images_not_yet_displayed.update(new_images)
    image_handler.all_images.update(new_images)


def its_time_to_update(ts):
    current_interval = time.time() - ts
    return current_interval > interval_between_images_in_seconds


imh.load_image()
timestamp = time.time()
print("Init Complete!")
while True:
    if its_time_to_update(timestamp):
        if my_obs.has_file_changes():
            load_new_images(my_obs, imh)

        imh.check_if_all_images_have_been_displayed_in_this_run_and_update_new_run_set()

        imh.load_image()
        timestamp = time.time()
