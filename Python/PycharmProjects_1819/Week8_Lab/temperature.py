"""Classes for working with Temperatures of different values.

Author: Brianna Guest
Class: CSI-260-02
Assignment: Week 8 Lab
Due Date: March 17, 2019 11:59 PM

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

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
           'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']


class TemperatureError(Exception):
    """Raises Error if degrees is not one of the specified forms."""

    def __init__(self, degrees):
        """Initialize exception with given username.

        Can optionally provide a user instance as well.
        """
        super().__init__(degrees)
        self.degrees = degrees

    def __str__(self):
        """Provide a string representation of the error."""
        return f'Invalid Value: {self.degrees}'


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees Celsius,
    or Kelvins.
    """

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees.

        Args:
            degrees, which can be one of the following:
                (1) a number, or a string containing a number
                    in which case it is interpreted as degrees Celsius
                (2) a string containing a number followed by one of the
                    following symbols:
                       C, in which case it is interpreted as degrees Celsius
                       F, in which case it is interpreted as degrees Fahrenheit
                       K, in which case it is interpreted as Kelvins

        Raises:
            InvalidTemperatureError: if degrees is not one of the specified
                                     forms

        """
        if type(degrees) is int or type(degrees) is float:
            self._celsius = float(degrees)
        elif type(degrees) is str:
            if degrees[-1] == 'C' and degrees[-2] != 'C':
                self._celsius = float(degrees[:-1])
            elif degrees[-1] == 'F':
                fahrenheit = float(degrees[:-1])
                self._celsius = ((fahrenheit - 32) * (5/9))
            elif degrees[-1] == 'K':
                kelvin = float(degrees[:-1])
                self._celsius = (kelvin - 273.15)
            elif degrees in NUMBERS:
                self._celsius = float(degrees)
            elif degrees[0] == '-':
                self._celsius = float(degrees)
            elif (degrees[0] in LETTERS) or (degrees[-1] != 'C') or \
                    (degrees[-1] != 'F') or (degrees[-1] != 'K'):
                raise TemperatureError(degrees)
        elif type(degrees) is not str or int:
            raise TemperatureError(degrees)
        self._degrees = degrees

    @property
    def celsius(self):
        """Degrees Celsius Property."""
        return self._celsius

    @celsius.setter
    def celsius(self, celsius):
        self._degrees = celsius

    @property
    def fahrenheit(self):
        """Degrees Fahrenheit Property to convert Celsius to Fahrenheit."""
        return (self._celsius * (9/5)) + 32

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        self._degrees = fahrenheit

    @property
    def kelvin(self):
        """Degrees Kelvin Property to convert Celsius to Kelvin."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, kelvin):
        self._degrees = kelvin

    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        total = 0
        for temp in temperatures:
            temp = Temperature(temp).celsius
            total = total + temp
        return total / len(temperatures)
