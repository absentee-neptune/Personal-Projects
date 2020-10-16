grade_percentage = int(input("Please enter your grade percentage: "))

# A+'s don't exist at Champlain
if grade_percentage >= 93:
    # if the grade is greater than or equal to 93
    print("Your letter grade is an A.")
elif grade_percentage >= 90 and grade_percentage <= 92:
    # if the grade is or between 90 and 92
    print("Your letter grade is an A-.")

elif grade_percentage >= 87 and grade_percentage <= 89:
    # if the grade is or between 87 and 89
    print("Your letter grade is a B+.")
elif grade_percentage >= 83 and grade_percentage <= 86:
    # if the grade is or between 83 and 86
    print("Your letter grade is a B.")
elif grade_percentage >= 80 and grade_percentage <= 82:
    # if the grade is or between 80 and 82
    print("Your letter grade is a B-.")

elif grade_percentage >= 77 and grade_percentage <= 79:
    # if the grade is or between 77 and 79
    print("Your letter grade is a C+.")
elif grade_percentage >= 73 and grade_percentage <= 76:
    # if the grade is or between 73 and 76
    print("Your letter grade is a C.")
elif grade_percentage >= 70 and grade_percentage <= 72:
    # if the grade is or between 70 and 72
    print("Your letter grade is a C-.")

elif grade_percentage >= 67 and grade_percentage <= 69:
    # if the grade is or between 67 and 69
    print("Your letter grade is a D+.")
elif grade_percentage >= 63 and grade_percentage <= 66:
    # if the grade is or between 63 and 66
    print("Your letter grade is a D.")
elif grade_percentage >= 60 and grade_percentage <= 62:
    # if the grade is or between 60 and 62
    print("Your letter grade is a D-.")

elif grade_percentage < 60:
    # if the grade is less than 60
    # (Could have also made this statement just an 'else' statement)
    print("Your letter grade is a F.")