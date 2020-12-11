#!/usr/bin/python3

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return None

def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.
    List must be sorted.
    """
    slist = sorted(list) #must be sorted
    print(slist)
    left = 0
    right = len(slist) - 1 #20 elements
    while left <= right:
        middle = (left + right) // 2
        print(f"This is middle in list: {middle}")
        
        if slist[middle] == key:
            return "Got it!", middle
        if slist[middle] > key:
            right = middle - 1
            print(right)
        if slist[middle] < key:
            left = middle + 1
            print(left)
    return None

thislist = ["apple", "banana", "cherry", "kiwi", "cherry", "radish", "scallion bunch", 'Apple Pie', 'Bacon', 'Chicken Pie', 'Chickpeas', 'Eggs', 'Milk', 'Pudding', 'Pulses', 'Rice', 'Rice Cooker', 'Sauce', 'bread', 'meat']

# print(linear_search(thislist, "banana"))
print(binary_search(thislist, "Eggs"))