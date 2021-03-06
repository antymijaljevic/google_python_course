#!/usr/bin/env python3

import csv
import re
import operator
import subprocess


def errorCounter():
    errorsDict = {}
    #open log file, slice, count
    with open("syslog.log") as log:
        log = log.readlines()

        for line in log:
            if "ERROR" in line:
                #search for ticket title
                sliceErrors = re.search(r"ERROR ([\w' ]*)", line)
                if sliceErrors[1] in errorsDict:
                    errorsDict[sliceErrors[1]] += 1
                else:
                    errorsDict[sliceErrors[1]] = 1

    #sort errors from highest to lowest, add header
    errorsDict = dict(sorted(errorsDict.items(), key = operator.itemgetter(1), reverse=True))
    header = {'Error': 'Count'}
    header.update(errorsDict)

    #create csv from sorted dictionary
    with open('error_message.csv', mode='w') as error_csv_file:
        csv_writer = csv.writer(error_csv_file)

        for key, value in header.items():
            csv_writer.writerow([key.strip(), value])


def userStatistics():
    ldapDict = {"Username":["INFO", "ERROR"]}
    #open log file, slice, count
    with open("syslog.log") as log:
        log = log.readlines()
        
        for line in log:
            #search for ldap
            ldap = re.search(r"\((\w.*)\)$", line)
            if "INFO" in line:
                if ldap[1].strip() in ldapDict:
                    ldapDict[ldap[1].strip()][0] += 1
                else:
                    ldapDict[ldap[1].strip()] = [0, 0]
                    ldapDict[ldap[1].strip()][0] = 1
            elif "ERROR" in line:
                if ldap[1].strip() in ldapDict:
                    ldapDict[ldap[1].strip()][1] += 1
                else:
                    ldapDict[ldap[1].strip()] = [0, 0]
                    ldapDict[ldap[1].strip()][1] = 1

    #sort ldaps by alphabetical order
    ldapDict = dict(sorted(ldapDict.items(), key = operator.itemgetter(0)))

    #create csv from sorted dictionary
    with open('user_statistics.csv', mode='w') as user_statistics_file:
        csv_writer = csv.writer(user_statistics_file)

        for key, value in ldapDict.items():
            csv_writer.writerow([key, value[0], value[1]])


def createHtml():
    #generate html file for error messages
    # args = ["./csv_to_html.py", "error_message.csv", "/var/www/html/errorIndex.html"] # activeate afer
    args = ["./csv_to_html.py", "error_message.csv", "/home/amijaljevic/Desktop/errorIndex.html"] # remove later
    subprocess.check_call(args)

    #generate html file for user statistics
    args[1] = "user_statistics.csv"
    # args[2] = "/var/www/html/usersIndex.html" #activate later
    args[2] = "/home/amijaljevic/Desktop/usersIndex.html" # remove later
    subprocess.check_call(args)


errorCounter()
userStatistics()
createHtml()

#---------------------------------------------------------------------------------------------
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
# involved. FILE: error_message.csv

#task 2
# The user usage statistics for the service: A list of all users 
# that have used the system, including how many info messages and
# how many error messages they've generated. This report is sorted 
# by username. FILE: user_statistics.csv