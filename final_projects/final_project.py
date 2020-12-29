#!/usr/bin/env python3

#1 | changeImage.py 

import os
from PIL import Image

images_dir = os.path.join(os.environ['HOME'] + '/final_projects/supplier-data/images/')

#list images, convert them to 600x400, jpeg format
for image in os.listdir(images_dir):
    print(image)
    if not image.startswith('.'):
        img = Image.open(images_dir + image).convert('RGB')
        img.resize((600,400)).save(images_dir + image+'.jpeg')





#2 | 