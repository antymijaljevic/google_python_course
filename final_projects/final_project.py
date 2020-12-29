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


#3 | run.py

import os
import requests

description_dir = os.path.join(os.environ['HOME'] + '/Documents/coding_projects/google_python_course/final_projects/supplier-data/descriptions/')

# list files from dir
for txtFile in os.listdir(description_dir):
    #print(txtFile)

    # Pre-setup dict
    descriptions_data = {'name': None, 'weight': None, 'description':None, 'image_name':None}
    order = list(descriptions_data)

    #open each file and create dict from info
    with open(os.path.join(description_dir, txtFile)) as contentOfFile:
        for index, line in enumerate(contentOfFile):
            descriptions_data[order[index]] = line.strip()

    #add .jpeg file to dict, set weight value to int for django model
    descriptions_data['image_name'] = os.path.basename(txtFile).replace('.txt', '.jpeg')
    descriptions_data['weight'] = int(descriptions_data['weight'].split()[0])

    print(descriptions_data)
    # #4 | post dict, clear dict
    # print(feedbacks)
    # response = requests.post('http://35.202.197.14/feedback', data=feedbacks)
    # feedbacks = {}

    # #5 | status code
    # if not response.ok:
    #     response.raise_for_status()
    # else:
    #     print("STATUS CODE 201 SUCCESS!")