"""Code for Week 3 Lab practicing creating a class.

Author: Brianna Guest
Class: CSI-260-02
Assignment: Week 3 Lab
Due Date: February 5, 2019 11:59 PM

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


class Country:
    """A single country.

    Attributes:
        name: string
        population: integer
        area: integer

    """

    def __init__(self, name, population, area):
        """Initialize the country information.

        :param: name: a string to represent the name of the country
        :param: population: an integer to represent the population of country
        :param: area: an integer to represent the area of the country
        """
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, country):
        """Compare the area of another country object to self.

        :return: Boolean
        """
        if self.area > country.area:
            return True
        else:
            return False

    def population_density(self):
        """Return the population density (people per square kilometer) of the country.

        :return: integer
        """
        pop_density = self.population / self.area
        return pop_density

    def summary(self):
        """Return a summary representing the country.

        :return: string
        """
        summary = self.name+" has a population of " + \
            str(self.population)+" people " \
            "and is "+str(self.area)+" square km. " \
            "It therefore has a population density of " \
            + str(f'{self.population_density():.4f}') + \
            " people per square km."
        return summary
