# Practice 1
'''
values = [i for i in range(1, 1001) if i % 7 == 0]

# or

# for i in range(0, 1001):
#    if i % 7 == 0:
#        values.append(i)

print(values)
'''

# Practice 2
'''
values = [i for i in range(1, 1001) if '3' in str(i)]
print(values)
'''

# Practice 3
'''
VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
statement = input("Enter a sentence: ")

no_vowel = ''.join([letter for letter in statement if letter not in VOWELS])
print(no_vowel)
'''

# Practice 4
'''
statement = input("Enter a sentence: ")
words = statement.split(" ")

list_words = [word for word in words if len(word) < 4]
print(list_words)
'''

# Practice 5

statement = input("Enter a sentence: ")
words = statement.split(" ")
stuff = {word: len(word) for word in words}

print(stuff)

