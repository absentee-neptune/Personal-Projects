#Anything highlighted I changed or added
#I mostly just changed how some stuff was worded (or added) in relation to the Algorithm given to make things clearer.
def fahrenheit_to_celsius(temp_fahrenheit):
    return ((5 / 9 * temp_fahrenheit) - 32)
def celsius_to_fahrenheit(temp_celsius):
    return ((9 / 5 * temp_celsius) + 32)

f_to_c = "C"
c_to_f = "F"
exit = "exit"

end_yes = "yes"
end_no = "no"

print("Hello!")
start_action = input("Which conversion would you like to do. Enter 'C' to convert to Celsius, 'F' to convert to Fahrenheit, or 'exit' to exit the program.")
w   hile start_action == f_to_c:
    f_temp = int(input("Enter the temperature in Fahrenheit: "))
    result_c = fahrenheit_to_celsius(f_temp)
    print(result_c)
    end_action = input("Would you like to perform another conversion? Type 'yes' to perform another one, or 'no' to exit the program.")
    if end_action == end_yes:
        start_action = input("Which conversion would you like to do. Enter 'C' to convert to Celsius, 'F' to convert to Fahrenheit, or 'exit' to exit the program.")
    else:
        print("Alright. Have a good day!")
        break

while start_action == c_to_f:
    c_temp = int(input("Enter the temperature in Celsius: "))
    result_f = celsius_to_fahrenheit(c_temp)
    print(result_f)
    end_action = input("Would you like to perform another conversion? Type 'yes' to perform another one, or 'no' to exit the program.")
    if end_action == end_yes:
        start_action = input("Which conversion would you like to do. Enter 'C' to convert to Celsius, 'F' to convert to Fahrenheit, or 'exit' to exit the program.")
    else:
        print("Alright. Have a good day!")
        break

while start_action == exit:
    print("Alright. Have a good day!")
    break


