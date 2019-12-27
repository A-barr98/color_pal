import os
from glob import glob
from PIL import Image


def sort_images(source, destination, extension):
    images = source.map_image_folder(source, extension)
    images = sort_by_avg_color(images)
    i = 0
    for image in images:
        image.image.save((os.path.join(destination, str(i)) + extension))
        i += 1


def map_image_folder(folder, extension):
    files = "*" + extension
    return map(Image.open, glob.glob(os.path.join(folder, files)))


def sort_by_avg_color(images):
    return images.sort(key=lambda img: avg_pix_col(img))


def avg_pix_col(image):
    image = image.resize((1, 1))
    return image.getpixel((0, 0))