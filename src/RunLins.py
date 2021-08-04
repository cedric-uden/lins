import time
from ConfigureLins import ConfigureLins


class RunLins:

    def __init__(self):
        self.conf = ConfigureLins()
        self.conf.imh.load_image()
        self.main_loop()

    def main_loop(self):
        timestamp = time.time()
        print("Init Complete!")
        while True:
            if self.its_time_to_update(timestamp):
                if self.conf.my_obs.has_file_changes():
                    self.load_new_images(self.my_obs, self.imh)

                self.conf.imh.check_if_all_images_have_been_displayed_in_this_run_and_update_new_run_set()
                self.conf.imh.load_image()
                timestamp = time.time()

    def load_new_images(self):
        new_images = self.conf.my_obs.get_and_clean_file_changes_set()
        self.conf.imh.new_images_not_yet_displayed.update(new_images)
        self.conf.imh.all_images.update(new_images)

    def its_time_to_update(self, ts):
        current_interval = time.time() - ts
        return current_interval > self.conf.interval_between_images_in_seconds
