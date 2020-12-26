#!/usr/bin/python3

#import libraries
import os
from PIL import Image

#working directories
images_dir = os.path.join(os.environ['HOME'] + '/images/')
destination_dir = '/opt/icons/'

#converter
for image in os.listdir(images_dir):
    if not image.startswith('.'):
        img = Image.open(images_dir + image).convert('RGB')
        img.rotate(-90).resize((128,128)).save(destination_dir + image, 'jpeg')


# test
# img = Image.open(destination_dir + 'ic_edit_location_black_48dp')
# print(img.format, img.size)