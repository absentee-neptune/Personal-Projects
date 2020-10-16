# The use of the [pyad] external library has been influenced from the Website:
    # https://github.com/zakird/pyad
    # All credit to the use of code from the [pyad] external library goes to Author Zakir Durumeric
    # License: Apache Software License (Apache License, Version 2.0)

# THIS PROGRAM CAN ONLY BE TESTED IN A SERVER ENVIRONMENT (sorry)

from pyad import pyad  # a just in case thing
from pyad import aduser  # imports code used for User manipulation in AD from the downloaded [pyad] library
from pyad import adgroup  # imports code used for Group manipulation in AD from the downloaded [pyad] library
from pyad import adcomputer  # imports code used for Computer manipulation in AD from the downloaded [pyad] library
from pyad import adcontainer  # imports code used for Active Directory container manipulation from the [pyad] library
import sys

# Admin Username and Password used for testing purposes
admin_username = "brianna.guest"
admin_password = "E10"

# The main menu for navigating the functions of the program
menu_text = "\n" \
            "| Welcome to Active Directory |" \
            "\n(1) Add Something" \
            "\n(2) Remove Something" \
            "\n(3) Manipulate Something" \
            "\n(4) Quit the Program" \

# The following three variables
#   is supposed to set the organizational units to send user, group, or computer information
#   for the create() and manipulate() functions, but there is an issue with server communication and they can't be used
#   therefore there are issues when using the create_whatever() and manipulate_whatever() functions
#   removing stuff works though

try:  # error handling
    users_ou = adcontainer.ADContainer.from_dn("ou=Users, dc=brianna, dc=local")
except:  # prints error in neater format and doesn't exit the program
    print("Unexpected Error: \n", sys.exc_info())
try:  # error handling
    groups_ou = adcontainer.ADContainer.from_dn("ou=Groups, dc=brianna, dc=local")
except:  # prints error in neater format and doesn't exit the program
    print("Unexpected Error: \n", sys.exc_info())
try:  # error handling
    computers_ou = adcontainer.ADContainer.from_dn("ou=Computers, dc=brianna, dc=local")
except:  # prints error in neater format and doesn't exit the program
    print("Unexpected Error: \n", sys.exc_info())


def create():
    """ Give Admin the option to create a User, Group, or Computer.
           It then navigates the Admin to the appropriate function to enter information.

    :return (if Option 1 was entered): (function) create_user()
    :return (if Option 2 was entered): (function) create_group()
    :return (if Option 3 was entered): (function) create_computer()
    """
    add_menu = "" \
               "| Choose a Class to Create |" \
               "\n(1) User" \
               "\n(2) Group" \
               "\n(3) Computer"
    print(add_menu)
    admin_choice = input("Enter here: ")

    if admin_choice == "1":  # sends the Admin to the create_user() function
        create_user()
    elif admin_choice == "2":  # sends the Admin to the create_group() function
        create_group()
    elif admin_choice == "3":  # sends the Admin to the create_computer() function
        create_computer()
    else:
        print("\n| Re-enter the option |\n")


def create_user():
    """ Creates a User in Active Directory based on the input given by the Admin

    :return: (string) The User has successfully been created
    """
    new_user = input("| Enter the name of the User | ")
    password = input("| Enter the Password of the User | ")
    try:  # error handling
        aduser.ADUser.create(new_user, container_object=none, password=password, enable=True)
        print("| User Created |")
    except:  # prints error in neater format and doesn't exit the program
        print("Unexpected Error: \n", sys.exc_info())


def create_group():
    """ Creates a Group in Active Directory based on the input given by the Admin

    :return: (string) The Group has successfully been created
    """
    new_group = input("| Enter the name of the Group | ")
    try:  # error handling
        adgroup.ADGroup.create(new_group, container_object=none, security_enabled=True, scope='GLOBAL')
        print("| Group created |")
    except:  # prints error in neater format and doesn't exit the program
        print("Unexpected Error: \n", sys.exc_info())


def create_computer():
    """ Creates a Computer in Active Directory based on the input given by the Admin

    :return: (string) The Computer has successfully been created
    """
    new_computer = input("| Enter the name of the Computer | ")
    try:  # error handling
        adcomputer.ADComputer.create(new_computer, container_object=none, enable=True)
        print("| Computer created |")
    except:  # prints error in neater format and doesn't exit the program
        print("Unexpected Error: \n", sys.exc_info())


def remove():
    """ Give Admin the option to remove a User, Group, or Computer.
        It then navigates the Admin to the appropriate function to enter information.

    :return (if Option 1 was entered): (function) remove_user()
    :return (if Option 2 was entered): (function) remove_group()
    :return (if Option 3 was entered): (function) remove_computer()
    """
    remove_menu = "" \
                  "| Choose a Class to Remove |" \
                  "\n(1) User" \
                  "\n(2) Group" \
                  "\n(3) Computer"
    print(remove_menu)
    admin_choice = input("Enter here: ")

    if admin_choice == "1":  # sends the Admin to the remove_user() function
        remove_user()
    elif admin_choice == "2":  # sends the Admin to the remove_group() function
        remove_group()
    elif admin_choice == "3":  # sends the Admin to the remove_computer() function
        remove_computer()
    else:
        print("\n| Re-enter the option |\n")


def remove_user():
    """ Removes a User in Active Directory based on the input given by the Admin

    :return: (string) The User has successfully been removed
    """
    user_input = input("| Enter the name of the User | ")
    try:  # error handling
        aduser.ADUser.from_cn(user_input).delete()
        print("| User removed |")
    except:  # prints error in neater format and doesn't exit the program
        print("Unexpected Error: \n", sys.exc_info())


def remove_group():
    """ Removes a Group in Active Directory based on the input given by the Admin

    :return: (string) The Group has successfully been removed
    """
    group_input = input("| Enter the name of the Group | ")
    try:  # error handling
        adgroup.ADGroup.from_dn(group_input).delete()
        print("| Group Removed |")
    except:  # prints error in neater format and doesn't exit the program
        print("Unexpected Error: \n", sys.exc_info())


def remove_computer():
    """ Removes a User in Active Directory based on the input given by the Admin

    :return: (string) The Computer has successfully been removed
    """
    computer_input = input("| Enter the name of the Computer | ")
    try:  # error handling
        adgroup.ADComputer.from_dn(computer_input).delete()
        print("| Computer Removed |")
    except:  # prints error in neater format and doesn't exit the program
        print("Unexpected Error: \n", sys.exc_info())


def manipulate():
    """ Give Admin the option to manipulate an appropriate attribute for a User or Group.
            It then navigates the Admin to the appropriate function to enter information.

    :return (if Option 1 was entered): (function) manipulate_user()
    :return (if Option 2 was entered): (function) manipulate_group()
    """
    manipulate_menu = "" \
                      "| Choose a Class to Manipulate |" \
                      "\n(1) User" \
                      "\n(2) Group"
    print(manipulate_menu)
    admin_choice = input("Enter here: ")

    if admin_choice == "1":  # sends the Admin to the manipulate_user() function
        manipulate_user()
    elif admin_choice == "2":  # sends the Admin to the manipulate_group() function
        manipulate_group()
    else:
        print("\n| Re-enter the option |\n")


def manipulate_user():
    """ Let's Admin manipulate attributes of an inputted User by either:
        1. Setting a Password
        2. Force the user to change the password at next login

    :return: (string) Success
    """
    user_manipulate = input("Enter name of User to Manipulate: ")
    manipulate_menu_user = "" \
                           "| Choose how to Manipulate |" \
                           "\n(1) Set Password" \
                           "\n(2) Force User to Change Password at next login"
    print(manipulate_menu_user)
    admin_choice = input("Enter here: ")

    if admin_choice == "1":  # set a password for a user
        try:  # error handling
            new_password = input("| Enter New Password | ")
            aduser.ADUser.set_password(user_manipulate, new_password)
            print("| Password Set |")
        except:  # prints error in neater format and doesn't exit the program
            print("Unexpected Error: \n", sys.exc_info())
    elif admin_choice == "2":  # force a user to change their password when they next login
        try:  # error handling
            aduser.ADUser.force_pwd_change_on_login(user_manipulate)
        except:  # prints error in neater format and doesn't exit the program
            print("Unexpected Error: \n", sys.exc_info())
    else:
        print("\n| Re-enter the option |\n")


def manipulate_group():
    """Let's Admin manipulate attributes of an inputted Group by either:
        1. Adding Members
        2. Removing Members
        3. Get a list of Members for a Group

    :return: (string) Success
    """
    group_manipulation = input("Enter name of Group to Manipulate: ")
    manipulate_menu_group = "" \
                            "| Choose how to Manipulate |" \
                            "\n(1) Add Member" \
                            "\n(2) Remove Member" \
                            "\n(3) Get list of Members"
    print(manipulate_menu_group)
    admin_choice = input("Enter here: ")

    if admin_choice == "1":  # Add a user to a group
        while True:
            user_add = input("Enter User (Press Enter to end): ")
            try:  # error handling
                adgroup.ADGroup.add_members(group_manipulation, user_add)
                print("| User Added |")
            except:  # prints error in neater format and doesn't exit the program
                print("Unexpected Error: \n", sys.exc_info())
            if user_add == "":
                break
    elif admin_choice == "2":  # removed a user from a group
        while True:
            user_remove = input("Enter User (Press Enter to end): ")
            try:  # error handling
                adgroup.ADGroup.add_members(group_manipulation, user_remove)
                print("| User Removed |")
            except:  # prints error in neater format and doesn't exit the program
                print("Unexpected Error: \n", sys.exc_info())
            if user_remove == "":
                break
    elif admin_choice == "3":  # Get a list of members from a group
        try:  # error handling
            adgroup.ADGroup.get_members(group_manipulation, recursive=False, ignoreGroups=False)
        except:  # prints error in neater format and doesn't exit the program
            print("Unexpected Error: \n", sys.exc_info())
    else:
        print("\n| Re-enter the option |\n")


while True:  # Log-in to get to the main menu of the Active Directory functions menu
    username_input = input("\nEnter username: ")
    password_input = input("Enter password: ")
    if password_input != admin_password:
        print("\n| Username or Password Unknown |\n")
    elif username_input != admin_username:
        print("\n| Username or Password Unknown |\n")
    elif username_input == admin_username and password_input == admin_password:
        break

while True:  # Navigation code for the main menu
    print(menu_text)
    admin_choice = input("\nEnter an option: ")

    if admin_choice == '1':  # create a user, group, or computer on Active Directory
        create()
    elif admin_choice == '2':  # remove a user, group, or computer on Active Directory
        remove()
    elif admin_choice == '3':  # manipulate user or group settings
        manipulate()
    elif admin_choice == '4':  # exit the program
        sys.exit()
    else:
        print("\n| Re-enter the option |\n")

