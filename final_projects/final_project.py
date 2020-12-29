#!/usr/bin/env python3

# #1 | changeImage.py 

# import os
# from PIL import Image

# images_dir = os.path.join(os.environ['HOME'] + '/supplier-data/images/')

# #list images, convert them to 600x400, jpeg format
# for image in os.listdir(images_dir):
#     if not image.startswith('.'):
#         img = Image.open(images_dir + image).convert('RGB')
#         img.resize((600,400)).save(images_dir + os.path.splitext(image)[0] +'.jpeg')



# #2 | supplier_image_upload.py

# import os
# import requests

# images_dir = os.path.join(os.environ['HOME'] + '/Documents/coding_projects/google_python_course/final_projects/supplier-data/images/')
# url = "http://<linux_instance_ip/upload/"

# #upload all .jpeg files
# for image in os.listdir(images_dir):
#     if image.endswith('.jpeg'):
#         with open(images_dir + image, 'rb') as opened:
#             r = requests.post(url, files = {'file': opened})

# #success or fail
# if not r.ok:
#     r.raise_for_status()
# else:
#     print("STATUS {} SUCCESS!".format(r.status_code))

