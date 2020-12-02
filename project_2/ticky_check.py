#!/usr/bin/env python3

#INFO/ERROR

# POSSIBLE ERRORS:

# - Timeout while retrieving information
# - The ticket was modified while updating
# - Connection to DB failed
# - Tried to add information to a closed ticket
# - Permission denied while closing ticket
# - Ticket doesn't exist

#POSSIBLE INFO
# - Created ticket
# - Closed ticket
# - Commented on ticket

#LOG EXAMPLE
# Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)
# Jan 31 20:21:55 ubuntu.local ticky: INFO Commented on ticket [#7159] (ahmed.miller)
# Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)
# Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)
# Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)

#TO GENERATE HTML FILE AND LOAD FILE ON SERVER
# ./csv_to_html.py user_emails.csv /var/www/html/<my_name>.html


#task 1
# The ranking of errors generated by the system: A list of all the error 
# messages logged and how many times each error was found, sorted by the most 
# common error to the least common error. This report doesn't take into account the users
# involved. FILE: user_statistics.csv


#task 2
# The user usage statistics for the service: A list of all users 
# that have used the system, including how many info messages and
# how many error messages they've generated. This report is sorted 
# by username. FILE: error_message.csv


#import all the shit
import os
import csv
import re
import operator


#ERRORS
errors = {}

#open log file, slice, count
with open("syslog.log") as log:
    log = log.readlines()

    for line in log:
        if "ERROR" in line:
            sliceErrors = re.search(r"ERROR ([\w' ]*)", line)
            if sliceErrors[1] in errors:
                errors[sliceErrors[1]] += 1
            else:
                errors[sliceErrors[1]] = 1

#sort errors from highest to lowest
errors = dict(sorted(errors.items(), key = operator.itemgetter(1), reverse=True))
# print(errors)

#create csv from sorted dictionary
for key, value in errors.items():
    print(key+" "+str(value))


#list all ldaps and how many info and how many error they had in total
with open("syslog.log") as log:
    log = log.readlines()

    for line in log:
        sliceLdaps = re.search(r"\((\w.*)\)$", line)
        # print(sliceLdaps[1].strip())



# #sort ldaps in list
# sorted(theList, key=operator.itemgetter(0))