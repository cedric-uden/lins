from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    print(f"hey, {event.src_path} has been created!")


class MyObserver:

    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True

    def __init__(self, path):

        self.my_event_handler = \
            PatternMatchingEventHandler(self.patterns,
                                        self.ignore_patterns,
                                        self.ignore_directories,
                                        self.case_sensitive)
        self.my_event_handler.on_created = on_created
        self.path = path

    def start_observer(self):
        go_recursively = True
        my_observer = Observer()
        my_observer.schedule(self.my_event_handler, self.path,
                             recursive=go_recursively)
        my_observer.start()
