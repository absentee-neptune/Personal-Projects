userList = []

while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        userList.append(newWord)

userList.insert(-1, "and")
print(*userList, sep=", ")  # code influenced from source: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
# I was having trouble trying to show the whole list and was able to find a way to do so from the website




