"""Tools for working with Temperatures.

Author: Brianna Guest
Class: CSI-260-02
Assignment: Week 8 Lab
Due Date: March 8, 2019 11:59 PM

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


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
        """
        self.celsius = degrees
        self._celsius = degrees

    def __str__(self):
        """Convert a Temperature instance to a string."""
        return f'{self._celsius}°C'

    def __repr__(self):
        """Convert a Temperature instance to an appropriate representation."""
        return f'Temperature({self._celsius!r})'

    def __eq__(self, other):
        """Compare two Temperature instances to see if they are equal."""
        if self._celsius is other:
            return True
        elif self._celsius != other:
            return False
        else:
            return True

    def __lt__(self, other):
        """Compare two Temperature instances.

        To see if one is less than another.
        """
        if Temperature(self.celsius < other.celsius) is True:
            return True
        else:
            return False

    def __gt__(self, other):
        """Compare two Temperature instances.

        To see is one is greater than another.
        """
        if Temperature(self.celsius > other.celsius) is True:
            return True
        else:
            return False

    def __le__(self, other):
        """Compare two Temperature instances.

        To see if one is less than or equal to another.
        """
        if self._celsius <= other:
            return True
        elif self._celsius >= other:
            return False
        else:
            return True

    def __ge__(self, other):
        """Compare two Temperature instances.

        To see if one is greater than or equal to another.
        """
        if self._celsius >= other:
            return True
        elif self._celsius <= other:
            return False
        else:
            return True

    def __add__(self, other):
        """Add two Temperature instances|Temperature instance and a number.

        The result must be a new Temperature instance.
        """
        try:
            return Temperature(self.celsius + other.celsius)
        except AttributeError:
            return Temperature(self.celsius + other)

    def __radd__(self, other):
        """Add two Temperature instances|Temperature instance and a number.

        The result must be a new Temperature instance.
        """
        return self + other

    def __sub__(self, other):
        """Subtract two Temperature instances|Temperature instance and a number.

        The result must be a new Temperature instance.
        """
        try:
            return Temperature(self.celsius - other.celsius)
        except AttributeError:
            return Temperature(self.celsius - other)

    def __rsub__(self, other):
        """Subtract two Temperature instances|Temperature instance and a number.

        The result must be a new Temperature instance.
        """
        return self + other

    def __iadd__(self, other):
        """Create new instances of Temperature and overwriting the old variable.

        The operation happens in-place.
        """
        self.celsius += other
        return self

    def __isub__(self, other):
        """Create new instances of Temperature and overwriting the old variable.

        The operation happens in-place.
        """
        self.celsius -= other
        return self

    def __hash__(self):
        """Hashes the Temperature Object.

        To be able to use Temperature objects as keys of a dictionary.
        """
        return hash(self._celsius)
