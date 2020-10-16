import math

def celcius_to_fahrenheit(temperature_in_celcius): #(parameter)
    #This function converts a number from Celcius to Farenheit
    #f = 9/5*c+32

    #Arguments:
        # temperature_in_celcius(float): The temperature to convert

    #Returns:
        #float: The temperature in Fahrenheit

    #Assumptions:
        #Assumes that temperature_in_celcius is a float

    return ((9 / 5 * temperature_in_celcius) + 32)

def fahrenheit_to_celcius(temperature_in_fahrenheit):
    return ((5 / 9 * temperature_in_fahrenheit) - 32)

print("Please enter 'F' to convert to Fahrenheit, 'C' to convert to Celcius, or 'E' to exit.")
action = input("Enter the function you wish to execute: ")

temperature_c = float(input("Enter the temperature in Celcius: "))
result_c = celcius_to_fahrenheit(temperature_c)
print(result_c)

temperature_f = float(input("Enter the temperature in Fahrenheit: "))
result_f = fahrenheit_to_celcius(temperature_f)
print(result_f)