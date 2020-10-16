# from random import randint
# # import [random] module
# random_num = randint(0, 9)
#
# while True:
#     guess = int(input("Guess a number between 0 and 9: "))
#
#     if random_num == guess:
#         # If the random number chosen by the module is the same as the guess input from the user
#         print("You guessed right!")
#     else:
#         # If the random number chosen by the module is NOT the same as the guess input from the user
#         print("Oops, you guessed wrong.")
#
#     try_again = input("Would you like to try again? Enter 'YES' or 'NO'")
#     if try_again == 'YES':
#         True
#     else:
#         break

# or

from random import randint
random_num = randint(0, 10)

for x in range(3):
    guess = int(input("Guess a number between 0 and 10: "))

    if random_num == guess:
        print("You guessed right!")

        try_again = input("Would you like to try again? Enter 'YES' or 'NO'")
        if try_again == 'YES':
            True
        else:
            break
    elif random_num < guess:
        print("Oops, you guessed too high.")
    elif random_num > guess:
        print("Oops, you guessed too low.")

print("Oops, you ran out of guesses.")