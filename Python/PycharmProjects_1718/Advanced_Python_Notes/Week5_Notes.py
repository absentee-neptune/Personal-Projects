# class A:
#     """An example parent class."""
#     def __init__(self, value):
#         """Initialize from provided value."""
#         self.value = value
#
#     def do_something(self):
#         """Do something interesting."""
#         print("do something")
#
#
# class B(A):
#     """An example child class (AKA subclass AKA derived class)"""
#     pass
#
#
# if __name__ == "__main__":
#     help(A)


class Person:
    """A person (base class)"""

    def __init__(self, name, id_number):
        """Initialize person with given name and id number."""
        self.name = name
        self.id_number = id_number


class Student(Person):
    """A student is a more specific type of person."""

    def __init__(self, name, id_number, major, graduation_year):
        """Initialize student with given name, id number, major, and graduation year."""
        super().__init__(name, id_number)
        self.major = major
        self.graduation_year = graduation_year


class Faculty(Person):
    def __init__(self, name, id_number, department, advisees=None):
        super().__init__(name, id_number)
        self.department = department
        if advisees is None:
            self.advisees = []
        else:
            self.advisees = advisees

    def __str__(self):
        result = f"{super().__str__()} teaches in the Dept. of {self.department}"

        return result


if __name__ == "__main__":
    joe = Student()