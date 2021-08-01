import platform


def get_system():
    platform_name = platform.platform()
    return platform_name.split("-")[0]


class Settings:

    def __init__(self):
        self.path = ""
        self.extension = ""
        self.canvas_width = 0
        self.canvas_height = 0
        self.start_x = 0
        self.start_y = 0

        self.get_settings()

    def get_settings(self):
        if get_system() == "Linux":
            return self.linux()
        elif get_system() == "macOS":
            return self.mac_os()
        else:
            return None

    def mac_os(self):
        self.path = "/Users/ced/Pictures/"
        self.extension = ".JPG"
        self.canvas_width = 1926
        self.canvas_height = 1086
        self.start_x = 1437
        self.start_y = -3

    def linux(self):
        self.path = "images/"
        self.extension = ".jpg"
        self.canvas_width = 2560
        self.canvas_height = 1400
        self.start_x = 1920
        self.start_y = 1120
