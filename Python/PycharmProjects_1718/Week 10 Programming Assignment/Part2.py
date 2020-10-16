user_string = input("Submit text here: ")
stringFreq = {}

user_string = user_string.split()  # splits the sentence up by word
for word in user_string:  # goes through the split string
    stringFreq.setdefault(word, 0)  # Sets each word counter to zero
    stringFreq[word] = stringFreq[word] + 1  # if word in string is found, adds one to the counter
# Took inspiration from class examples from Week 9

print(stringFreq)
