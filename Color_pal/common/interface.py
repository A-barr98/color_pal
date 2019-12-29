from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from . import core

window = Tk()
window.title("Color Pal - The Color Palette Sorting Tool")
source_label = Label(window, text="Source Folder - Folder containing images to be sorted")
source_path_label = Label(window, text="<---- Select Your Folder")
extension_label = Label(window, text="File Extension - Sort all images of this file type")
extension_combo = Combobox(window)
extension_combo['values'] = (".jpeg", ".BMP", ".GIF")
dst_label = Label(window, text="Destination Folder - Where to output the sorted folders")
dst_path_label = Label(window, text="<--- Select Your Folder")


def source_button_clicked():
    source_dir = filedialog.askdirectory()
    source_path_label.configure(text=source_dir)


def dst_button_clicked():
    dst_dir = filedialog.askdirectory()
    dst_path_label.configure(text=dst_dir)


def go_button_clicked():
    core.sort_images(window.source_dir, window.dst_dir, extension_combo.get())


source_button = Button(window, text="Open", command=source_button_clicked)
dst_button = Button(window, text="Open", command=dst_button_clicked)
go_button = Button(window, text="Sort", command=go_button_clicked)
source_label.grid(column=0, row=0)
source_button.grid(column=0, row=1)
source_path_label.grid(column=1, row=1)
extension_label.grid(column=0, row=2)
extension_combo.grid(column=0, row=3)
dst_label.grid(column=0, row=4)
dst_button.grid(column=0, row=5)
dst_path_label.grid(column=1, row=5)
go_button.grid(column=1, row=6)

window.mainloop()
