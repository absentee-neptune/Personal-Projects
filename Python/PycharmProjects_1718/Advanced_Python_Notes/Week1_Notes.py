# Error Handling
'''
while True:
    try:
        x = int(input("Enter a number: "))
        print(x ** 2)
        break
    except ValueError:  # only executed when that particular error comes up in the code
        print("That was not a valid integer, please try again.")
    finally:  # always going to be executed
        print("In finally block")
'''

'''
# Comprehension
values = list(range(10))
print(values)

squares = []
squares_dictionary = {}
for value in values:
    if value % 2 == 0:
        squares.append(value ** 2)
    squares_dictionary[value] = value ** 2
print(squares)
print(squares_dictionary)

def square_value(x):  # Not an Important example
    return x ** 2
squares2 = list(map(square_value, values))
print(squares2)

squares3 = [value ** 2 for value in values if value % 2 == 0]
print(squares3)

squares_dictionary2 = {value: value ** 2 for value in values}
print(squares_dictionary2)
'''

# finding values (enumerate, zip)
values = ['hello', 'world', 'cool']
for index, value in enumerate(values):
    print(index, value)

other_values = [34, 45, 78]
for value, other in zip(values, other_values):
    print(value, other)


