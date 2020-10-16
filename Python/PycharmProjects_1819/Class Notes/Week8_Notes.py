"""
sequential search = start at the beginning
binary search = ordered list and a more faster/efficient way, calculates the midpoint, evaluate search item,determines direction, starts search

if you know the list is ordered use binary, other than that use sequential (may turn up errored results)
"""
'''
# Sequential Search Program
from random import randint
search_data = [i for i in range(1, 101)]
search_item = randint(1, 100)

finder = 0

for i in search_data:
    if i

if finder == 0:
    print("The value of " + str(search_item) + " is not in the list ")
else:
    print("The value of " + str(search_item) + " is in the list.")
'''


#  Binary Search Program
#  Found in http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
def binarySearch(alist, item):
    # The function has two placeholders
    first = 0  # to accept values when the function is called
    last = len(alist)
    found = False  # assume the search criteria is not found
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True  # If the search value is found then the variable 'found'
            # has its value changed from 'False' to 'True'
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found  # This has the function return a 'false' or a value of 0

'''
find = 8

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
search = binarySearch(testlist, find)
# if

if search == True:
    print("The value " + str(find) + " was found.")
else:
    print("The value " + str(find) + " was found in the list.")
'''

# Example
finder = 0
letters = ['D', 'J', 'k', 'l', 'E', 'f', 'L', 'c', 'G', 'h', 'i']
ltr = 'd'
for i in letters:
    if i == ltr:
        finder = i
        break
    else:
        continue

'''        
if finder == 0:
    print("The value of " + ltr + " was not found.")
else:
    print("The value of " + ltr + " was in the list.")

order_letters = letters
order_letters.sort(key=str.lower)
'''

# Example
search_letters = [ord(i) for i in letters]
user_input = input("Enter a letter you wish to search dor in the list: ")
ascii_equiv = ord(user_input)


def binarySearch2(alist, item):
    first = 0  # to accept values when the function is called
    last = len(alist)
    found = False  # assume the search criteria is not found
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True  # If the search value is found then the variable 'found'
            # has its value changed from 'False' to 'True'
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found  # This has the function return a 'false' or a value of 0


searching = binarySearch2(search_letters, ascii_equiv)
if finder == 0:
    print("The value of " + chr(ascii_equiv) + " was not found.")
else:
    print("The value of " + chr(ascii_equiv) + " was in the list.")
