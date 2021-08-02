import os
from PIL import ImageTk, Image
from Window import Window
from Settings import Settings


class ImageHandler:

    window = Window()
    settings = Settings()

    hot_folder_path = settings.path
    image_extension = settings.extension

    canvas_width = settings.canvas_width
    canvas_height = settings.canvas_height
    start_x = settings.start_x
    start_y = settings.start_y

    counter_all_displayed_images = 0

    all_images = set()

    current_run_images = set()

    new_images = set()
    new_images_not_yet_displayed = set()

    image_id = window.create_canvas_and_get_id()

    def load_all_image_paths(self):
        for path, dirs, files in os.walk(self.hot_folder_path):
            for filename in files:
                if filename[-len(self.image_extension):] == self.image_extension:
                    self.all_images.add(self.hot_folder_path + filename)

    def choose_image_to_load_next(self):
        if len(self.new_images_not_yet_displayed) > 0:
            return Image.open(self.new_images_not_yet_displayed.pop())
        else:
            return Image.open(self.current_run_images.pop())

    def set_aspect_ratio(self, pil_image):
        img_w, img_h = pil_image.size
        ratio = min(self.canvas_width / img_w, self.canvas_height / img_h)
        img_w = int(img_w*ratio)
        img_h = int(img_h*ratio)
        return pil_image.resize((img_w, img_h), Image.ANTIALIAS)

    def load_image(self):

        self.counter_all_displayed_images += 1
        pil_image = self.choose_image_to_load_next()
        image = ImageTk.PhotoImage(self.set_aspect_ratio(pil_image))
        self.window.canvas.itemconfig(self.image_id, image=image)
        self.window.root.update()

    def update_current_run_images(self):
        self.current_run_images = set()
        self.current_run_images.update(self.all_images)
        self.counter_all_displayed_images = 0

    def check_if_all_images_have_been_displayed_in_this_run_and_update_new_run_set(self):
        if self.counter_all_displayed_images == len(self.all_images):
            self.update_current_run_images()
