import csv
import sys

#The password list - We start with it populated for testing purposes
entries = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]

#The password file name to store the passwords to
password_file_name = "samplePasswordFile"

#The encryption key for the caesar cypher
encryption_key = 16

menu_text = """
What would you like to do:
1. Open password file
2. Lookup a password
3. Add a password
4. Save password file
5. Print the encrypted password list (for testing)
6. Quit program
Please enter a number (1-6)"""

def password_encrypt(unencrypted_message, key):
    """Returns an encrypted message using a caesar cypher

    :param unencrypted_message (string)
    :param key (int) The offset to be used for the caesar cypher
    :return (string) The encrypted message
    """

    #Fill in your code here.
    # #If you can't get it working, you may want to put some temporary code here
    # #While working on other parts of the program
    result = ''
    index = 0
    while index < len(unencrypted_message):
        ascii_val = ord(unencrypted_message[index]) - 32 + key
        ascii_val = ascii_val % (126 - 32)
        ascii_val += 32
        result = result + chr(ascii_val)

        index += 1
    return result
    # Placeholder for now, this is the Caesar Cipher example from class, going to try to write a simpler one
    pass

def load_password_file(file_name):
    """Loads a password file.  The file must be in the same directory as the .py file

    :param file_name (string) The file to load.  Must be a .csv file in the correct format
    :return (list) The password entries
    """
    with open(file_name, newline='') as csvfile:
        password_reader = csv.reader(csvfile)
        password_entries = list(password_reader)

    return password_entries

def save_password_file(password_entries, file_name):
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    with open(file_name, 'w+', newline='') as csvfile:
        password_writer = csv.writer(csvfile)
        password_writer.writerows(password_entries)

def add_entry(website, password):
    """Adds an entry with a website and password

    Logic for function:

    Step 1: Use the password_encrypt() function to encrypt the password.
            The encryptionKey variable is defined already as 16, don't change this
    Step 2: create a list of size 2, first item the website name and the second
            item the password.
    Step 3: append the list from Step 2 to the password list


    :param website (string) The website for the entry
    :param password (string) The unencrypted password for the entry
    """
    #Fill in your code here
    encrypt_password = password_encrypt(password, encryption_key)
    entries.append([website, encrypt_password])
    pass

def lookup_password(website):
    """Lookup the password for a given website

    Logic for function:
    1. Create a loop that goes through each item in the password list
     You can consult the reading on lists in Week 5 for ways to loop through a list

    2. Check if the name is found.  To index a list of lists you use 2 square bracket sets
      So passwords[0][1] would mean for the first item in the list get it's 2nd item (remember, lists start at 0)
      So this would be 'XqffoZeo' in the password list given what is predefined at the top of the page.
      If you created a loop using the syntax described in step 1, then i is your 'iterator' in the list so you
      will want to use i in your first set of brackets.

    3. If the name is found then decrypt it.  Decrypting is that exact reverse operation from encrypting.  Take a look at the
    caesar cypher lecture as a reference.  You do not need to write your own decryption function, you can reuse passwordEncrypt

     Write the above one step at a time.  By this I mean, write step 1...  but in your loop print out every item in the list
     for testing purposes.  Then write step 2, and print out the password but not decrypted.  Then write step 3.  This way
     you can test easily along the way.

    :param website (string) The website for the entry to lookup
    :return: Returns an unencrypted password.  Returns None if no entry is found
    """
    #Fill in your code here
    for i in entries:
        # NOT FINAL since not really a loop through the list
        if website == 'yahoo':
            password = entries[0][1]
            password = password_encrypt(password, encryption_key)
            return password
        elif website == 'google':
            password = entries[1][1]
            password = password_encrypt(password, encryption_key)
            return password
    pass

while True:
    print(menu_text)
    choice = input()

    if(choice == '1'):  # Load the password list from a file
        entries = load_password_file(password_file_name)

    if(choice == '2'): # Lookup at password
        print("Which website do you want to lookup the password for?")
        for key_value in entries:
            print(key_value[0])
        website = input()

        password = lookup_password(website)
        if password:
            print('The password is: ', password)
        else:
            print('Password not found')

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        password = input()
        add_entry(website, password)

    if(choice == '4'): #Save the passwords to a file
            save_password_file(entries, password_file_name)

    if(choice == '5'): #print out the password list
        for key_value in entries:
            print(', '.join(key_value))

    if(choice == '6'):  #quit our program
        sys.exit()