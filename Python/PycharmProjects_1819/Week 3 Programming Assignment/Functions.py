#Week 3 Programming Assignment - Functions

import math

def miles_to_kilometers(length_in_miles):
    # This function converts a number from miles to kilometers

    # Arguments:
    #     length_in_miles(float): The length to convert

    # Returns:
    #     float: The length in kilometers

    # Assumptions:
    #     Assumes that the length in miles is a float
    return (length_in_miles * 1.609)

miles_input = float(input("Enter the length in Miles: "))
result_kilometer = miles_to_kilometers(miles_input)
print(result_kilometer)

def pounds_to_grams(weight_in_pounds):
    # This function converts a number from pounds to pounds to grams
    #
    # Arguments:
    #     weight_in_pounds(float): The weight to convert
    #
    # Returns:
    #     float: The weight in grams
    #
    # Assumptions:
    #     Assumes that the weight in pounds is a float
    return (weight_in_pounds * 453.592)

pounds_input = float(input("Enter the weight in Pounds: "))
result_grams = pounds_to_grams(pounds_input)
print(result_grams)

def britishGallon_to_americanGallon(volume_in_britishGallon):
    # This function converts a number from British Gallons to U.S. Gallons
    #
    # Arguments:
    #     volume_in_britishGallon(float): The volume to convert
    #
    # Returns:
    #     float: The volume in U.S. Gallons
    #
    # Assumptions:
    #     Assumes that the volume in British Gallons is a float
    return (volume_in_britishGallon * 1.201)

britishGallon_input = float(input("Enter the volume in British Gallons: "))
result_americanGallon = britishGallon_to_americanGallon(britishGallon_input)
print(result_americanGallon)

def power_formula(work, time):
    # This function figures the amount of Power in Watts used by using two numerical inputs, Work and Time
    # Power = Work / time
    #
    # Arguments:
    #     work (float): The force to be divided (in Joules)
    #     time (float): The amount of time to divide by (in seconds)
    #
    # Returns:
    #     float: The amount of Power in Joules per second
    #
    # Assumptions:
    #     Assumes the amount of Work is a float
    #     Assumes that the amount of Time is a float
    return (work / time)

work_input = float(input("Enter the amount of Work in Joules: "))
time_input = float(input("Enter the amount of Time in seconds: "))
result_power = power_formula(work_input, time_input)
print(result_power)
