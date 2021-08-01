from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyObserver:

    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    has_file_changes = False

    def __init__(self, path):
        self.my_event_handler = \
            PatternMatchingEventHandler(self.patterns,
                                        self.ignore_patterns,
                                        self.ignore_directories,
                                        self.case_sensitive)
        self.path = path

    def on_created(self, event):
        print(f"hey, {event.src_path} has been created!")
        self.has_file_changes = True

    def start_observer(self):
        self.my_event_handler.on_created = self.on_created
        go_recursively = True
        my_observer = Observer()
        my_observer.schedule(self.my_event_handler, self.path,
                             recursive=go_recursively)
        my_observer.start()
