import screeninfo


class ScreenInfo:

    def __init__(self):
        self.all_monitors = screeninfo.get_monitors()
        self.number_of_screens = len(self.all_monitors)

    def print(self):
        for m in self.all_monitors:
            print(str(m))

    def get_primary(self):
        for m in self.all_monitors:
            if m.is_primary:
                return m
