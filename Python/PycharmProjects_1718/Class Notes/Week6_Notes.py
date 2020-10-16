# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]  # list concatenation
# print('The cat names are:')
# for name in catNames:
#     print('  ' + name)

#  method = any action we can take upon an object
#  property = a characteristic/descriptor
#  object = any thing that can be in memory

# products = [19.99, "Computer 1", 27]
# while True:
#     price = (input("Enter the product price or press enter to continue: "))
#     prod_desc = input("Enter the product name or press enter to continue: ")
#     monitor = (input("Enter the product size or press enter to continue: "))
#     if price == '' or prod_desc == '' or monitor == '':
#         break
#     products = products + [price] + [prod_desc] + [monitor]
# print(products)

names = ["John", "Betty", "Zak", "Mark", "Mary", "Kylie"]

# Returns the index value of an element in the list
# a = names.index('Zak')
# print(a)

# This is a ValueError message because 'Charles' is not in the list
# b = names.index("Charles")
# print(b)

# The append() will insert an element at the end of a list
names.append("Amos")
# print(names)

# The insert() method will allow the programmer to target a position in the list to insert a value
names.insert(3, "Steve")
# print(names)

names.remove("Mark")
# print(names)

# When performing a sort(), it will not work on a mixed list(ie. integers/alpha chars.)
names.sort()
# print(names)

# names.sort(reverse=True)
# print(names)

# userInput = input("Search for a name here: ")
# if userInput in names:
#     print('The name of ' + userInput + ' was found and will be removed.')
#     names.remove(userInput)
# elif userInput not in names:
#     print('The name of ' + userInput + ' was not found.')

# or

# def findName():
#     print('Here are the names in the list: ')
#     print(names)
#     j = 0
#     my_name = input('What name do you want removed: ')
#     for i in range(len(names)):
#         if my_name in names:
#             names.remove(my_name)
#             j = 1
#         else:
#             continue
#     if j == 1:
#         print('The value of ' + my_name + ' was found and removed: ')
#         print(names)
#     else:
#         print('The value of ' + my_name + ' was not found')

# findName()

# Nested loop is a loop in a loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
people = ["Andy", "Betsy", "Charles", "David", "George", "Harry", "Larry", "Mary", "Rose"]

for i in range(len(numbers)):
    for j in range(len(people)):
        # print("Person Num. " + str(numbers[i]) + ' is ' + people[j] + '.')
        placeOfPeople = str(numbers[i]) + ". " + people[i]
    print(placeOfPeople)

