from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from Settings import Settings


# source: http://thepythoncorner.com/dev/how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/


def get_empty_set():
    return set()


class MyObserver:

    settings = Settings()
    patterns = [settings.extension]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True

    def __init__(self, path):
        self.my_event_handler = \
            PatternMatchingEventHandler(self.patterns,
                                        self.ignore_patterns,
                                        self.ignore_directories,
                                        self.case_sensitive)
        self.path = path
        self.new_files = get_empty_set()
        self.deleted_files = get_empty_set()

    def has_file_changes(self):
        if len(self.new_files) > 0:
            return True
        else:
            return False

    def on_created(self, event):
        self.new_files.add(event.src_path)

    def on_deleted(self, event):
        self.deleted_files.add(event.src_path)

    def clean_file_changes_set(self):
        self.new_files = get_empty_set()

    def get_and_clean_file_changes_set(self):
        return_set = self.new_files
        self.clean_file_changes_set()
        return return_set

    def has_found_deleted_files(self):
        return not len(self.deleted_files) == 0

    def clean_deleted_set(self):
        self.deleted_files = get_empty_set()

    def start_observer(self):
        self.my_event_handler.on_created = self.on_created
        self.my_event_handler.on_deleted = self.on_deleted
        go_recursively = False
        my_observer = Observer()
        my_observer.schedule(self.my_event_handler, self.path,
                             recursive=go_recursively)
        my_observer.start()
