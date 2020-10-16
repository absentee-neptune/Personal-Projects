num_input1 = int(input("Enter a number: "))
num_input2 = int(input("Enter another number: "))
num_sum = num_input1 + num_input2
# sum of the two number inputs

if num_sum > 100:
    # If the sum of the two number inputs is greater than 100
    print("They add up to a big number.")
elif num_sum <= 100:
    # If the sum of the two number inputs is less than or equal to 100
    # (Could have also made this just an else statement)
    print("They add up to " + str(num_sum) + ".")