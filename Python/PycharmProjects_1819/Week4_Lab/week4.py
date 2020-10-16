"""Menu as User Interface for medical.py classes.

Authors: Cyprien Debargue, Brianna Guest
Class: CSI-260-02
Assignment: Week 4 Lab
Due Date: February 12, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import sys
import csv
from medical import Patient, Procedure

main_menu = "Patient Database Main Menu" \
            "\n" \
            "1. Search Patient Database by ID Number" \
            "\n2. Add New Patient" \
            "\n3. Quit" \
            "\n"

patient_menu = "Patient Information Menu" \
               "\n" \
               "1. Modify Patient Information" \
               "\n2. Delete Patient" \
               "\n3. Add a Procedure" \
               "\n"

modification_menu = "Modification Menu" \
                    "\n" \
                    "1. First Name" \
                    "\n2. Last Name" \
                    "\n3. Address" \
                    "\n4. Phone Number" \
                    "\n5. Emergency Contact First Name" \
                    "\n6. Emergency Contact Last Name" \
                    "\n7. Emergency Contact Phone Number" \
                    "\n"


def main():
    """Main Menu for Patient Information and commands associated with the menu options."""
    # Patient.load_patients()  # Load pickled dictionary from file

    print(main_menu)
    user_input = input("Enter Option: ")

    if user_input == '1':  # Search for Patient
        patient_id = input("Enter Patient ID Number: ")
        Patient.get_patient(patient_id)
        if None:
            print("Patient ID Not Found")
        else:
            print(patient_menu)
            user_input = input("Enter Option: ")

            if user_input == '1':  # modify Patient attributes
                print(modification_menu)
                user_input = input("Enter Option: ")

                if user_input == '1':  # Modify Patient First Name
                    new_fname = input("Enter Modification Here: ")
                    Patient.first_name = new_fname
                elif user_input == '2':  # Modify Patient Last Name
                    new_lname = input("Enter Modification Here: ")
                    Patient.last_name = new_lname
                elif user_input == '3':  # Modify Patient Address
                    new_phone = input("Enter Modification Here: ")
                    Patient.phone_number = new_phone
                elif user_input == '4':  # Modify Patient Phone Number
                    new_address = input("Enter Modification Here: ")
                    Patient.address = new_address
                elif user_input == '5':  # Modify Emergency Contact First Name
                    new_emergency_fname = input("Enter Modification Here: ")
                    Patient.emergency_fname = new_emergency_fname
                elif user_input == '6':  # Modify Emergency Contact Last Name
                    new_emergency_lname = input("Enter Modification Here: ")
                    Patient.emergency_lname = new_emergency_lname
                elif user_input == '7':  # Modify Emergency Contact Phone Number
                    new_emergency_phone = input("Enter Modification Here: ")
                    Patient.emergency_phone = new_emergency_phone

            elif user_input == '2':  # delete Patient
                confirmation = input("Re-enter Patient ID Number to Confirm: ")
                if confirmation == patient_id:
                    Patient.delete_patient(patient_id)
                else:
                    print("Patient ID - No Match")

            elif user_input == '3':  # add a procedure
                Patient.add_procedure()

    elif user_input == '2':  # Add a Patient
        first_name = input("Enter Patient's First Name: ")
        last_name = input("Enter Patient's Last Name: ")
        address = input("Enter Patient's Address: ")
        phone_number = input("Enter Patient's Phone Number: ")
        emergency_fname = input("Enter the Emergency Contact's First Name: ")
        emergency_lname = input("Enter the Emergency Contact's Last Name: ")
        emergency_phone = input("Enter the Emergency Contact's Phone Number: ")

        patient = [Patient(first_name, last_name, address, phone_number, emergency_fname, emergency_lname,
                           emergency_phone).to_string()]

        with open('database.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == first_name and line[2] == last_name and line[3] == address:
                    print("The Patient is already in the Database")
                else:
                    break

            with open('database.csv', 'a') as write_file:
                writer = csv.writer(write_file)
                writer.writerow(patient)
                print("Patient added")

    elif user_input == '3':  # Save and Quit
    #   Patient.save_patients()
        sys.exit()


if __name__ == '__main__':
    main()
