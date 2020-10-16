# Nested Loops
for column in range(1, 11):
    for row in range(1, 11):
        mult_num = row * column
        if mult_num < 10:
            space = '  '
        elif mult_num < 90:
            space = ' '
        print(space + str(mult_num), end = ' ')
    print()

# or

for i in range(1, 11):
    if(i < 10):
        print("i = ", i, ":", end=" ")
    else:
        print("i =", i, ":", end=" ")
    for j in range(1, 11):
        print("{:0>3d}".format(i * j), end=" ")
    print()

# Ciphers and Caesar Cipher
def password_encrypt (unencryptedMessage, key):
    """Returns an encrypted message using a caesar cypher
    
    :param unencryptedMessage (string)
    :param key (int) The offset to be used for the caesar cypher
    :return (string) The encrypted message
    
    1.  Create a result string
    2.  Loop through each character of the unencryptedMessage
    3.  Convert to the ASCII Value
    4.  Subtract 32
    5.  Add the key
    6.  Modularly divide by (126 - 32) to shift back to a valid range
    7.  Add 32 back to the number
    8.  Convert back to a character
    9.  Append onto the end of the result string
    10.  Return the result string
    """

    result = ''
    index = 0
    while index < len(unencryptedMessage):
        ascii_val = ord(unencryptedMessage[index]) - 32 + key
        ascii_val = ascii_val % (126 - 32)
        ascii_val += 32
        result = result + chr(ascii_val)

        index += 1
    return result

print(password_encrypt("Hi",5))
