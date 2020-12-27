#!/usr/bin/env python3

import os
import requests


#1 | list feedbacks from dir
for txtFile in os.listdir('/data/feedback/'):
    # print(txtFile)

    #2 | Pre-setup dict, list indexing
    feedbacks = {'title': None, 'name': None, 'date':None, 'feedback':None}
    order = list(feedbacks)

    #3 | open each feed back and create dict
    with open(os.path.join('/data/feedback', txtFile)) as contentOfFile:
        for index, line in enumerate(contentOfFile):
            feedbacks[order[index]] = line.strip()

    #4 | post dict, clear dict
    print(feedbacks)
    response = requests.post('http://35.202.197.14/feedback', data=feedbacks)
    feedbacks = {}

    #5 | status code
    if not response.ok:
        response.raise_for_status()
    else:
        print("STATUS CODE 201 SUCCESS!")