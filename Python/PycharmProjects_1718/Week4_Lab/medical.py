"""Management of Patient and Procedure Information.

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
import pickle
import csv


class Patient:
    """A patient's personal information.

    Attributes:
        first_name: string
        last_name: string
        address: string
        phone_number: integer
        emergency_fname: string
        emergency_lname: string
        emergency_phone: integer
        id_num: integer
    """
    _next_id = 0
    #_all_patients = {}

    def __init__(self, first_name, last_name, address, phone_number, emergency_fname, emergency_lname, emergency_phone):
        """Initializes Patient information

        :param first_name: a patient's first name
        :param last_name: a patient's last name
        :param address: a patient's address
        :param phone_number: a patient's phone number
        :param emergency_fname: emergency contact's first name
        :param emergency_lname: emergency contact's last name
        :param emergency_phone: emergency contact's phone number
        """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.emergency_fname = emergency_fname
        self.emergency_lname = emergency_lname
        self.emergency_phone = emergency_phone
        self.id_num = Patient._next_id
        Patient._next_id += 1

        #_all_patients[self.id_nums] = self

    def to_string(self):
        string = f"Patient ID Number: {self.id_num}" \
            f"\nPatient: {self.first_name} {self.last_name} " \
            f"\nAddress: {self.address} " \
            f"\nPhone Number: {self.phone_number} " \
            f"\nEmergency Contact: {self.emergency_fname} {self.emergency_lname} " \
            f"\nEmergency Phone Number: {self.emergency_phone}"

        print(string)

    @classmethod
    def get_patient(cls, id_num):
        """Takes the ID number of a patient and returns the Patient information if the entry exists.

        :return None or Patient Information
        """
        # for Patient.id in Patient._all_patients:
        #     if id_num == Patient.id in Patient._all_patients:
        #         return Patient._all_patients[Patient.id].to_string()
        #     else:
        #         return None

        with open('database.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == id_num:
                    Patient(line[0], line[1], line[2], line[3], line[4], line[5], line[6]).to_string()
                else:
                    return None

    @classmethod
    def delete_patient(cls, id_num):
         """Takes the ID number of a patient and deletes the entry from the [_all_patients] dictionary."""
        # for Patient.id in Patient._all_patients:
        #     if id_num == Patient.id in Patient._all_patients:
        #         return Patient.id
        #     else:
        #         return None
         with open('database.csv', 'r') as bye_data, open('database_delete.csv', 'w') as data_out:
            writer = csv.writer(data_out)
            for row in csv.reader(bye_data):
                if row[0] == id_num:
                    writer.writerow(row)
                else:
                    return None

    # @classmethod
    # def save_patients(cls):
    #     """Saves the [_all_patients] dictionary to a file."""
    #     pickle.dump(Patient._all_patients, open("pickle.txt", 'wb'))
    #
    # @classmethod
    # def load_patients(cls):
    #     """Loads the dictionary from a file, and then appropriately sets the next
    #             available ids for patients and procedures so that newly added
    #             patients will still get a unique id."""
    #     infile = open("pickle.txt", 'rb')
    #     Patient._all_patients = pickle.load(infile)
    #     infile.close()
    #     return Patient._all_patients

    # @classmethod
    # def save_patients(cls):
    #     with open('database.csv', 'r') as csv_file:
    #         csv_reader = csv.reader(csv_file)
    #         for line in csv.reader(csv_file):
    #             if line[0] == Patient.id_num
    #
    # @classmethod
    # def load_patients(cls):
    #

    @classmethod
    def add_procedure(cls):
        name = input("Enter Name of Procedure: ")
        date = input("Enter Date of Procedure: ")
        med_practitioner = input("Enter Medical Practitioner: ")
        cost = input("Enter Cost of Procedure: ")

        Procedure(name, date, med_practitioner, cost).to_string()


class Procedure:
    """A Patient's procedure information.

    Attributes:
        name: string
        date: string
        med_practitioner: string
        cost: integer
        id_num : integer
    """
    _num_procedures = 0

    def __init__(self, name, date, med_practitioner, cost):
        """Initializes a Patient's procedure information.

        :param name: a procedures name
        :param date: the date of the procedure
        :param med_practitioner: the medical practitioner performing the procedure
        :param cost: the procedures cost
        """

        self.name = name
        self.date = date
        self.med_practitioner = med_practitioner
        self.cost = cost

        Procedure._num_procedures += 1
        self.id_num = Procedure._num_procedures

    def to_string(self):
        string = f"Procedure ID Number: {self.id_num}" \
            f"\nProcedure Name: {self.name}" \
            f"\nProcedure Date: {self.date}" \
            f"\nMedical Practitioner: {self.med_practitioner} " \
            f"\nCost of Procedure: {self.cost}"

        print(string)

