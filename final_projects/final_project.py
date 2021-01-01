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

# import os, requests

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




# #3 | run.py

# import os, requests

# description_dir = os.path.join(os.environ['HOME'] + '/Documents/coding_projects/google_python_course/final_projects/supplier-data/descriptions/')

# # list files from dir
# for txtFile in os.listdir(description_dir):
#     #print(txtFile)

#     # Pre-setup dict
#     descriptions_data = {'name': None, 'weight': None, 'description':None, 'image_name':None}
#     order = list(descriptions_data)

#     #open each file and create dict from info
#     with open(os.path.join(description_dir, txtFile)) as contentOfFile:
#         for index, line in enumerate(contentOfFile):
#             descriptions_data[order[index]] = line.strip()

#     #add .jpeg file to dict, set weight value to int for django model
#     descriptions_data['image_name'] = os.path.basename(txtFile).replace('.txt', '.jpeg')
#     descriptions_data['weight'] = int(descriptions_data['weight'].split()[0])

#     print(descriptions_data)
#     #post to server and return status code
#     response = requests.post('https://<linux_instance_ip/fruits', json=descriptions_data)
#     if not response.ok:
#         response.raise_for_status()
#     else:
#         print("STATUS {} SUCCESS!".format(response.status_code))

#     #empty dict
#     descriptions_data = {}


#4 | reports.py

import reportlab

def generate_report():
    pass

#attachment argument (use ‘/tmp/processed.pdf')

# Processed Update on <Today's date>

# [blank line]

# name: Apple

# weight: 500 lbs

# [blank line]

# name: Avocado

# weight: 200 lbs

# [blank line]



# 5| report_email.py

import os, datetime, reports


def main():
    reports.generate_report(attachment, title, paragraph)

if __name__ == "__main__":
    main()



# 6| emails.py



# 7| health_check.py