#Conversation with a Computer - Week 2 Assignment

fname = input("Hello! What is your name?")

age = int(input("Hi " + fname + ". How old are you?"))
if age <= 38:
    print("Wow, you're " + str(age) + ". You are so young.")#response that uses user input
if age > 38:
    print("Wow, you're " + str(age) + ". Some people would call you old.")#response that uses user input
#I included the [fname] variable in the question of the input of the [age] variable to help reuse variables
#I also included if statements to help create responses from the user input

pizza_opinion = input("Do you like pizza?")
if pizza_opinion == "yes":
    print("That's cool, so do I.")
    pizza_choice = input("What kind of pizza do you like?")
    print("You like " + pizza_choice + "? That's awesome, I like that too.")#response that uses user input
if pizza_opinion == "no":
    print("Oh wow, you must be crazy.")
#just some yes or no questions to (again) easily create if statements to create responses from the user input

chocolate_opinion = input("Do you also like chocolate?")
if chocolate_opinion == "yes":
    print("That's awesome.")
if chocolate_opinion == "no":
    print("wait WHAT?!")
#again the same

tv_hours = int(input("How many hours do you usually watch TV in a week, " + fname + "?"))
music_hours = int(input("How many hours in a week do you also usually listen to music, " + fname + "?"))
computer_hours = int(input("...and on a computer?"))
total_hours = tv_hours + music_hours + computer_hours #an arithmetic operation that uses user input
hours_day = total_hours // 7 #another arithmetic operation that uses user input in a different way to create a different answer by using the output of [total_hours]
if total_hours < 40:
    print("That's " + str(total_hours) + " hours a week.")#response that uses the sum of the user inputs
    print("So that's about " + str(hours_day) + " hours a day.")#response that still uses the sum of the user input in a different algorithm
    print("Oooo, that's not a lot of time with technology at all during the week.")
if total_hours >= 40:
    print("That's " + str(total_hours) + " hours a week.")#response that uses the sum of the user inputs
    print("So that's about " + str(hours_day) + " hours a day.")#response that still uses the sum of the user input in a different algorithm
    print("Oh no, that's a lot of time with technology. You should go outside more often.")