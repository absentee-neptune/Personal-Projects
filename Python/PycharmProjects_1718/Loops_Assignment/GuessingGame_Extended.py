from random import randint
# import [random] module
randomNum = randint(1, 100)
# a random integer would be chosen from between 1 and 100

name = input("Hi! What is your name? ")

while True:
# Keeps the following code in a loop until the guess is answered correctly

    try:
        guess = int(input("Please guess a number between 1 and 100, " + name + ": "))
    except ValueError:
        print("Uh-ooooohhhhh...(POOF)")
        break
    # the above code was influenced by this source: https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    # I just tried to find something that would recognize that if user input was not an integer it would let the user try again or end the program

    if guess == randomNum:
        # If the random number chosen by the module is the same as the guess integer from the user
        print("Congratulations, you guessed it!")
        break
    elif guess < 1 or guess > 100:
        # If the guess integer from the user is not between 1 and 100
        print("Uh-ooooohhhhh...(POOF)")
        break
    elif guess < randomNum:
        # If the guess integer from the user is less than the chosen random integer
        print("You guessed too low, try again.")
    elif guess > randomNum:
        # If the guess integer from the user is less than the chosen random integer
        print("You guessed too high, try again.")
