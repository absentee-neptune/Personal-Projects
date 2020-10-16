listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

print(listToPrint[0], end="")
for i in range(1, len(listToPrint)-1):
    print(",", listToPrint[i], end="")
print(", and", listToPrint[-1], end="")
