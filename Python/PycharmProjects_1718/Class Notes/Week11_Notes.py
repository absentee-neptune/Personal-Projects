import csv
import sys

menu_text = "" \
            "\nWhat would you like to do:" \
            "\n(1) Find a customer" \
            "\n(2) Remove a duplicate record" \
            "\n(3) Add a customer" \
            "\n(4) Quit the program" \
            ""


def search_customer(cfn, cln):
    with open('customer_data.csv', 'r') as csv_file:  # Open the file in 'read' mode
        csv_reader = csv.reader(csv_file)  # Create a variable 'csv_reader', pass file contents to it
        counter = 0
        for line in csv_reader:  # reading EVERY line of data in the file
            if line[1] == cfn and line[2] == cln:  # Once the first and last name in the variables match a line
                                                    # in the file, we get the email address of that customer
                print("E-mail Address of " + cfn + " " + cln + ": " + line[3])  # email address is shown here
                counter += 1
    if counter > 1:
        print("\nThe customer " + cfn + " " + cln + " appears " + str(counter) + " times in the file.")


def delete_customer():
    '''
    cfn = input("\nPlease enter the customer's first name: ")
    cln = input("Please enter the customer's last name: ")

    with open('customer_data.csv', 'r') as csv_file:  # Open the file in 'read' mode
        csv_reader = csv.reader(csv_file)  # Create a variable 'csv_reader', pass file contents to it
        counter = 0
        for line in csv_reader:  # reading EVERY line of data in the file
            if line[1] == cfn and line[2] == cln:  # Once the first and last name in the variables match a line
                                                    # in the file, we get the email address of that customer
                if counter == 0:
                    print("E-mail Address of " + cfn + " " + cln + ": " + line[3])  # email address is shown here
                    counter += 1
                elif counter > 1:
                    with open('customer_delete.csv', 'w') as bye_data:  # Open the file in 'write' mode
                        csv_writer = csv.writer(bye_data)
                        csv_writer.writerow(line)
    '''
    cfn = input("\nPlease enter the customer's first name: ")
    cln = input("Please enter the customer's last name: ")
    cem = input("Please enter the customer's e-mail address: ")

    with open('customer_data.csv', 'r') as bye_data, open('customer_delete.csv', 'w') as data_out:
        writer = csv.writer(data_out)
        counter = 0
        for row in csv.reader(bye_data):
            if row[1] == cfn and row[2] == cln and row[3] == cem and counter == 0:
                counter += 1
            elif row[1] == cfn and row[2] == cln and row[3] == cem and counter == 1:
                writer.writerow(row)
            else:
                print("| System Failure | Please Try Again |")


def add_customer():
    cid = input("\nCustomer ID: ")
    cfn = input("Customer's first name: ")
    cln = input("Customer's last name: ")
    cem = input("Customer's e-mail address: ")
    file_data = [cid, cfn, cln, cem]

    with open('customer_data.csv', 'r') as csv_file:  # Open the file in 'read' mode
        csv_reader = csv.reader(csv_file)  # create a variable 'csv_reader', pass the file contents to it
        for line in csv_reader:  # reading every line of data in the file
            if line[0] == cid and line[1] == cfn and line[2] == cln and line[3] == cem:
                print("| The Customer is Already in the Database |")
            else:
                break
    with open('customer_data.csv', 'a') as write_file:
        writer = csv.writer(write_file)
        writer.writerow(file_data)
        print("| Customer Added |")


def user_input():  # This function will allow a user to identify a customer for search
    cfn = input("\nPlease enter the customer's first name: ")
    cln = input("Please enter the customer's last name: ")

    return search_customer(cfn, cln)  # Pass the values of the user's input to a function call
    # Return the results variable


while True:
    print(menu_text)
    choice = input("Please enter an option: ")

    if choice == '1':
        user_input()
    elif choice == '2':
        delete_customer()
    elif choice == '3':
        add_customer()
    elif choice == '4':
        sys.exit()
    else:
        print("\n| Please re-enter an option |")
