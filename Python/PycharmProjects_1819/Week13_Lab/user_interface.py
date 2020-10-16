"""User Interface for medical database.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

import models


def add_doctor():
    """User Interface for adding a new doctor to the database."""
    params = dict()
    params['first_name'] = input('First Name? ')
    params['last_name'] = input('Last Name? ')
    params['primary_office'] = input('Primary Office? ')
    new_doc = models.Doctor(**params)
    new_doc.save()


def add_patient():
    """User Interface for adding a new patient to the database."""
    params = dict()
    params['first_name'] = input('First Name? ')
    params['last_name'] = input('Last Name? ')
    params['address'] = input('Address? ')
    params['phone_number'] = input('Phone Number? ')
    params['emergency_contact'] = input('Emergency Contact? ')
    params['emergency_phone'] = input('Emergency Phone? ')

    response = input('Do you want to assign a primary care doctor (Y/N)? ')

    if response.lower() in ('y', 'yes'):
        params['primary_care_doctor'] = pick_primary_care_doctor()

    new_patient = models.Patient(**params)
    new_patient.save()


def pick_primary_care_doctor():
    """User Interface for selecting a primary care doctor.

    Return: A Doctor object.  Returns None if no doctor selected.
    """
    doc_name = input('Identify a Doctor by last name or press enter to '
                     'display all doctors? ')
    if doc_name:
        docs = models.Doctor.select().where(models.Doctor.last_name
                                            == doc_name)
    else:
        docs = models.Doctor.select()
    if docs.count() > 1:
        for i, doc in enumerate(docs):
            print(f'{i}. Dr. {doc.first_name} {doc.last_name}')
        while True:
            doc_choice = input('Choose by number? ')
            try:
                return(docs[int(doc_choice)])
            except (IndexError, ValueError):
                print('Invalid choice')
    elif docs.count() == 1:
        print('Only one matching Doctor found')
        print(f'Assigning Dr. {docs[0].first_name} '
              f'{docs[0].last_name} to patient')
        return docs[0]
    else:
        print('No doctor found with that name.')
        response = input('Skip choosing primary care doctor (Y/N)')
        if response.lower() in ('y', 'yes'):
            return None
        return pick_primary_care_doctor()


def add_procedure():
    """User interface for adding a procedure to the database."""
    params = dict()
    params['name'] = input('Procedure Name? ')
    params['min_cost'] = input('Minimum Cost? ')
    params['max_cost'] = input('Maximum Cost? ')
    params['pre_procedure_checklist'] = input('Pre-Procedure Checklist? ')

    new_procedure = models.Procedure(**params)
    new_procedure.save()


def add_performed_procedures():
    """User interface to add performed procedures to database."""
    params = dict()
    params['patient'] = input('Patient? ')
    params['doctor'] = input('Doctor? ')
    params['procedure'] = input('Procedure Name? ')
    params['procedure_date'] = input('Procedure Date? ')
    params['notes'] = input("Notes? ")

    new_performed_procedures = models.PerformedProcedure(**params)
    new_performed_procedures.save()


if __name__ == "__main__":
    DONE = "done"
    menu_dict = {'1': add_doctor,
                 '2': add_patient,
                 '3': add_procedure(),
                 '4': add_performed_procedures(),
                 '5': None,
                 '6': None,
                 '7': None,
                 '8': DONE}
    menu = """
1. Add Doctor
2. Add Patient
3. Add Procedure
4. Add Performed Procedure
5. Lookup a patient's medical records
6. Add a medication to the list of available prescriptions
7. Assign a medication to a patient
8. Quit
Choose:
"""
    while True:
        user_choice = input(menu)
        if user_choice in menu_dict and menu_dict[user_choice]:
            if menu_dict[user_choice] == DONE:
                break
            menu_dict[user_choice]()
        else:
            print('Not a valid choice')
