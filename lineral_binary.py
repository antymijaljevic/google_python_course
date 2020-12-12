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
        print(f"This is middle in list: {middle}, {slist[middle]}")
        
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

print(linear_search(thislist, "banana"))
print(binary_search(thislist, "Rice"))





def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  list = sorted(list)
  middle = len(list)//2
  if list[middle] == item:
    return True

  # print(list)
  # print(list[middle], middle)
  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False