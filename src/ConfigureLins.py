import FileSystemWatchdog
from Settings import Settings
from ImageHandler import ImageHandler


class ConfigureLins:

    def __init__(self):
        self.settings = Settings()
        self.hot_folder_path = self.settings.path
        self.interval_between_images_in_seconds = self.settings.interval_between_images_in_seconds
        self.imh = ImageHandler()
        self.imh.load_all_image_paths()
        self.imh.update_current_run_images()
        self.my_obs = FileSystemWatchdog.MyObserver(self.hot_folder_path)
        self.my_obs.start_observer()
