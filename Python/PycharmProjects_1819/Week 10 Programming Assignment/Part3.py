user_string = input("Submit text here: ")
stringFreq = {}

user_string = user_string.split()
# splits the sentence up by word and returns it back into the same variable
for word in user_string:  # goes through the split string
    stringFreq.setdefault(word, 0)  # Sets each word counter to zero
    stringFreq[word] = stringFreq[word] + 1  # if word in string is found, adds one to the counter
# Took inspiration from class examples from Week 9

print("\nTotal number of words in the given string: " + str(len(user_string)))
# This reads the length of the string (in words) and prints the output


stringFreq = sorted(stringFreq.items(), key=lambda kv: kv[1], reverse=True)
# This sorts the the words by the frequency from greatest to least and returns it back into the same variable

print("\nThe top 20 most frequently-used words in the given string:")
for key, value in stringFreq[:20]:
    print("'" + key + "': " + str(value))
    # Got help from website: (and realized I was using the wrong variable)
    # https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values


freqPercentage = [(instance, count / len(user_string)) for instance, count in stringFreq]
# This calculates the percentage each word will occur by using the total length of the string
# and the frequency in which they occurred

print("\nThe chances that those words will occur again:")
for word, percentage in freqPercentage[:20]:
    print("'%s': %.2f%%" % (word, percentage * 100))
    # Got help from website:
    # https://stackoverflow.com/questions/52871769/python-calculate-word-frequency-in-percentage






