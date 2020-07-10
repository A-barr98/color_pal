import os
import sys
from glob import glob
from PIL import Image


def run():
    src = sys.argv[1]
    dst_path = os.path.join(src, "sorted")
    os.mkdir(dst_path)
    sort_images(src=src, dst=dst_path, ext=get_ext(src))
    print("Done!")

def get_ext(src):
    # Assumes that all images follow the same format, gets file extension of the first image
    first_img = os.listdir(src)[0]
    filename, file_extension = os.path.splitext(first_img)
    return file_extension


def sort_images(src, dst, ext):
    # Sorts images and saves them into folder in the source directory
    imgs = []
    for filename in os.listdir(src):
        if filename.endswith(ext):
            imgs.append(os.path.join(src, filename))
    imgs = sort_by_avg_color(imgs)
    i = 0
    for img in imgs:
        img = Image.open(img)
        img.save(os.path.join(dst, (str(i)+ext)))
        i += 1
        img.close()


def sort_by_avg_color(images):
    # Sorts list of images
    images.sort(key=lambda image: avg_pix_col(image))
    return images


def avg_pix_col(image):
    # Gets the average pixel of image by reducing resolution to 1px by 1px
    with Image.open(image) as image:
        image = image.resize((1, 1))
        return image.getpixel((0, 0))


run()
