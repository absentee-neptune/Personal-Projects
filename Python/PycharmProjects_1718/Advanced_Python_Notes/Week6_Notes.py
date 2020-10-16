""" Abstract Base Classes
        abstract vs. concrete/tangible
        abstract class contains at least 1 abstract method
            CANNOT MAKE INSTANCES OF ABSTRACT CLASSES

    Duck Typing and EAFP (easier to ask for forgiveness than permission) vs. LBYL (Look before you leap)"""

# shapes.py (review on multiple inheritances)
import abc
import math


class Shape(abc.ABC):
    """Shape abstract base class that other class will implement from."""

    def __init__(self, color):
        """Create a shape of a specified color."""
        self.color = color

    @abc.abstractmethod
    def get_area(self):
        """Return the area of this shape.

        This must be implemented by all concrete subclasses.
        """
        pass


class Circle(Shape):
    """Circle is a concrete extension of Shape.

    :
    """

    def __init__(self, color, radius):
        """Create a circle of specified color and radius."""
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        """Return the area of this circle."""
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """ """
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


def print_area(shape):
    # LBYL
    # if hasattr(shape, "get_area") and callable(shape.get_area):
    #     print(f"{shape.get_area():.2f}")
    # else:
    #     print("Not a Shape!")

    # EAFP
    try:
        print(f"{shape.get_area():.2f}")
    except (TypeError, AttributeError):
        print("Not a Shape!")


class NotAShape:
    def __init__(self):
        pass

    def get_area(self, x):
        return 42
    # def get_area(self):
    #     return 42


if __name__ == "__main__":
    circle = Circle("red", 2)
    print_area(circle)

    rectangle = Rectangle("blue", 3, 5)
    print_area(rectangle)

    not_a_shape = NotAShape()
    print_area(not_a_shape)

