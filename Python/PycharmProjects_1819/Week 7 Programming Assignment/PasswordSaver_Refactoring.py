import csv
import sys

# The password list - We start with it populated for testing purposes
entries = {1: {'website': 'yahoo', 'username': 'jblumberg', 'password': 'XqffoZeo'},
           2: {'website': 'google', 'username': 'jackieb', 'password': 'CoIushujSetu'}}

# The password file name to store the passwords to
password_file_name = "samplePasswordFile"

# The encryption key for the caesar cypher
encryption_key = 16

menu_text = """
What would you like to do:
1. Open password file
2. Lookup a password
3. Add an entry
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

    # Fill in your code here.
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
    # This is the Caesar Cipher example from class
    
    pass


def load_password_file(file_name):
    """Loads a password file.  The file must be in the same directory as the .py file

    :param file_name (string) The file to load.  Must be a .csv file in the correct format
    :return (list) The password entries
    """
    # Code influenced from website:
    # https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        entries_file = list(reader)

    return entries_file


def save_password_file(entries_file, file_name):
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    # Code influenced from website:
    # https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
    with open(file_name, 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in entries.items():
            writer.writerow([key, value])


def add_entry(website, username, password):
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
    # Fill in your code here
    count = len(entries) + 1
    entries[count] = {}
    encrypt_password = password_encrypt(password, encryption_key)  # encrypts the password
    entries[count]['website'] = website  # adds website to the appropriate entry in the nested dictionary
    entries[count]['username'] = username  # adds username to the appropriate entry in the nested dictionary
    entries[count]['password'] = encrypt_password  # adds encrypted password to the appropriate entry in the nested list
    # Code was influenced from website: https://www.programiz.com/python-programming/nested-dictionary
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
    # Fill in your code here
# I got help for this part from:
# https://www.reddit.com/r/learnpython/comments/2ttuwa/python_27_searching_nested_dictionary/
    for key, value in entries.items():
        if entries[key]['website'] == website:
            return password_encrypt(entries[key]['password'], -16)
    pass


while True:
    print(menu_text)
    choice = input()

    if(choice == '1'):  # Load the password list from a file
        try:  # error handling
            entries = load_password_file(password_file_name)
        except FileNotFoundError:
            print("The file was not found.")

    if(choice == '2'):  # Lookup at password
        print("Which website do you want to lookup the password for?")
        # for key in entries.items():
        #     print(entries.get('website', 0))
        count = 1
        while count <= len(entries):
            print(entries[count]['website'])
            count += 1
        website = input()

        password = lookup_password(website)
        if password:
            print('The password is: ', password)
        else:
            print('Password not found')

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the username?")
        username = input()  # adds ability to add username for the add_entry function
        print("What is the password?")
        password = input()
        while len(password) < 6:  # Password must meet a requirement and loops until it is met
            print("Password length must contain at least 6 characters. Please enter a new password: ")
            password = input()
        add_entry(website, username, password)

    if(choice == '4'):  # Save the passwords to a file
            save_password_file(entries, password_file_name)

    if(choice == '5'):  # print out the entries dictionary
        for e_id, e_info in entries.items():
            print("\nEntry:", e_id)
            for key in e_info:
                print(key + ':', e_info[key])
    # Code was influenced from website: https://www.programiz.com/python-programming/nested-dictionary

    if(choice == '6'):  # quit our program
        sys.exit()
