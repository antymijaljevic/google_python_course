#!/home/amijaljevic/anaconda3/bin/python3
import os
import re
os.system('clear')


result = re.sub(r"[.?!]", "", "Love is here! Another one? This is last.")

print(result)
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])

# print("{} {}".format(result[2], result[1]))

# def rearrange_name(name):
#     result = re.search(r"^(\w*), (\w*)$", name)

#     if result is None:
#         return name

#     return "{} {}".format(result[2], result[1])

# print(rearrange_name("Lovelace, Ada"))

# print(rearrange_name("Ritchie, Dennis"))

# print(rearrange_name("Hopper, Grace M."))

regex = r"\[(\d+)\]"

result = re.search(regex, "a scary [cat] ghost appeared")

print(result)