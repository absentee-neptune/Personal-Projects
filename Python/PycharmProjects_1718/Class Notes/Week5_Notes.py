# y = 1, 2, 3, 4, 5
# for x in y:
#     print(x)

# for x in range(0, 11, 2):
#     print("The value in this range equals: ", x)

# x = 0
# while x < 10:
#     print("The value of x is", x)
#     break

# recursive 'for' loop (?)
# y = [1, 2, 3]
# for x in y:
#     y.append(x)
#     print(x)

# import random
# for i in range(5):
#     print(random.randint(1, 10))

# from random import randint
# random_num = randint(0, 10)
#
# for x in range(3):
#     guess = int(input("Guess a number between 0 and 10: "))
#
#     if random_num == guess:
#         print("You guessed right!")
#
#         try_again = input("Would you like to try again? Enter 'YES' or 'NO'")
#         if try_again == 'YES':
#             True
#         else:
#             break
#     elif random_num < guess:
#         print("Oops, you guessed too high.")
#     elif random_num > guess:
#         print("Oops, you guessed too low.")
#
# print("Oops, you ran out of guesses.")

# Class Example Game
# name = input("What is your name? ")
# number = random.randint(1, 10)
# counter = 0
# print(number)
# y = 1, 2, 3
# for x in y:
#     z = int(input("Hello " + name + ", please guess a number between 1 and 10: "))
#     counter += 1
#     if z == number:
#         print("Congratulations, you guessed it!")
#         break
#     elif z < number:
#         print("You guessed too low, try again an you have " + str(3-counter) + "guesses left.")
#     elif z > number:
#         print("You guessed too high, try again an you have " + str(3-counter) + "guesses left.")
#     else:
#         print("The system just blew up, it's over...")
#         break


# LISTS
# list = holds multiple items (array) / brackets are symbolic (all values are indexed)

y = ["A", "B", "C", "D"]
z = ["E", "F", "G", "H", "I", "J", "K", "L"]
# print(y[0])

# y.append(z)

list_x = y + z
# print(y + z)
# print(list_x)

# length = len(list_x)
# print(length)

# list_a = list_x - z
# print(list_a)

# for i in range(length):
#     print(list_x[i] + " is an element of the list 'x'.")

# user_input = input("What letter are you trying to find in the list: ")
# if list_x.index(user_input):
#     print("YES")
# else:
#     print("NO")

# half = len(list_x) // 2
# print(half)

#Print quarters of the list
fourth_a = list_x[0:3]
fourth_b = list_x[3:6]
fourth_c = list_x[6:9]
fourth_d = list_x[9:13]

print(fourth_a)
print(fourth_b)
print(fourth_c)
print(fourth_d)

#or

a = 0
b = c = len(list_x) // 4
for i in range(len(list_x) // c):
    print(list_x[a:b])
    a = b
    b += c