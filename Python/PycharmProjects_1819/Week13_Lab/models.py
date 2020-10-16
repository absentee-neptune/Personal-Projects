"""ORM Models for a patient database.

Also includes code to build the database if it doesn't exist.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

import peewee


database = peewee.SqliteDatabase("patient_database.sqlite")


class BaseModel(peewee.Model):
    """Base ORM model."""

    class Meta:
        """Common model configuration."""

        database = database

    def __str__(self):
        """Return string representation of record."""
        pass


class Procedure(BaseModel):
    """ORM model of procedures table."""

    name = peewee.CharField()
    min_cost = peewee.DecimalField(default=None)
    max_cost = peewee.DecimalField(default=None)
    pre_procedure_checklist = peewee.TextField(default='')

    class Meta:
        """Model configuration for procedures."""

        table_name = 'procedures'

    def __str__(self):
        """Return string representation of record."""
        return f'Procedure: {self.name}; {self.min_cost} to {self.max_cost};' \
            f' {self.pre_procedure_checklist}'


class Doctor(BaseModel):
    """ORM model of doctors table."""

    first_name = peewee.CharField()
    last_name = peewee.CharField()
    primary_office = peewee.CharField(default='')

    class Meta:
        """Model configuration for doctors."""

        table_name = 'doctors'

    def __str__(self):
        """Return string representation of record."""
        return f'Dr. {self.first_name} {self.last_name}; {self.primary_office}'


class Patient(BaseModel):
    """ORM model of patients table."""

    first_name = peewee.CharField()
    last_name = peewee.CharField()
    address = peewee.CharField(default='')
    phone_number = peewee.CharField(default='')
    emergency_contact = peewee.CharField(default='')
    emergency_phone = peewee.CharField(default='')
    primary_care_doctor = peewee.ForeignKeyField(Doctor, backref='patients',
                                                 null=True, default=None)

    class Meta:
        """Model configuration for patients."""

        table_name = 'patients'

    def __str__(self):
        """Return string representation of record."""
        return f'Patient: {self.first_name} {self.last_name}; {self.address};' \
            f' {self.phone_number}; {self.primary_care_doctor}' \
            f'Emergency Contact: {self.emergency_contact}; {self.phone_number}'


class PerformedProcedure(BaseModel):
    """ORM model of performed_procedures table."""

    patient = peewee.ForeignKeyField(Patient, backref='procedure_history')
    doctor = peewee.ForeignKeyField(Doctor, backref='procedure_history')
    procedure = peewee.ForeignKeyField(Procedure, backref='procedure_history')
    procedure_date = peewee.DateField(default=None)
    notes = peewee.TextField(default='')

    class Meta:
        """Model configuration for performed procedures."""

        table_name = 'performed_procedures'

    def __str__(self):
        """Return string representation of record."""
        return f'Patient: {self.patient} Doctor: {self.doctor}' \
            f'Procedure: {self.procedure}; {self.procedure_date}' \
            f'Notes: {self.notes}'


if __name__ == "__main__":
    try:
        Procedure.create_table()
    except peewee.OperationalError:
        print("Procedure table already exists!")

    try:
        Doctor.create_table()
    except peewee.OperationalError:
        print("Doctor table already exists!")

    try:
        Patient.create_table()
    except peewee.OperationalError:
        print("Patient table already exists!")

    try:
        PerformedProcedure.create_table()
    except peewee.OperationalError:
        print("performed_procedures table already exists!")
