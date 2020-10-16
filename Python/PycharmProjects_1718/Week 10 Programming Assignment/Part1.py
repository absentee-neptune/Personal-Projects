import string
user_string = input("Submit text here: ")

user_string = user_string.lower()  # changes all uppercase letter to lowercase
user_string = user_string.replace(' ', '')  # deletes all the whitespace by replacing the spaces with non-spaces
for x in string.punctuation:
    user_string = user_string.replace(x, '')
    # this loop goes through each punctuation character and removes it from the string
    # by replacing it with nothing (the empty quotations)

print(user_string)
