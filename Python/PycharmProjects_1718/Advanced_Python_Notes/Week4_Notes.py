class Employee:
    num_employees = 0
    raise_amount = 1.05

    def __init__(self, first_name, last_name, salary):
        """Initialize an Employee with given names and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Employee.num_employees += 1  # it would be global.-- if variable was outside class
        self.id = Employee.num_employees

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def increase_raise_amount(cls, percentage):
        cls.raise_amount += percentage  # if @staticmethod, have to hard  code Employee.raise_amount


def main():
    john = Employee("John", "Smith", 45000)
    jane = Employee("Jane", "Doe", 60000)

    jane.raise_amount = 1.1
    jane.apply_raise()

    print(john.__dict__)
    print(jane.__dict__)


if __name__ == "__main__":
    main()

