import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("display image")
im=Image.open("images/2.jpg")
photo=ImageTk.PhotoImage(im)
cv = tk.Canvas()
root.attributes('-fullscreen', True)
cv.pack(side='top', fill='both', expand=True)
cv.create_image(0, 0, image=photo, anchor='nw')
root.mainloop()
