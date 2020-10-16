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

    attributes:
        color: string
        radius: number
    """
    def __init__(self, color, radius):
        """Create a circle of specified color and radius."""
        super().__init__(color)
        self.radius = radius

    @property
    def get_area(self):
        """Return the area of this circle."""
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"A {self.color} circle with radius {self.radius} and area {self.get_area}"

    # code representation of string (python readable)
    def __repr__(self):
        return f"Circle({self.color!r}, {self.radius})"

    def __add__(self, other):
        try:
            return Circle(self.color + "-" + other.color, self.radius + other.radius)
        except AttributeError:
            return Circle(self.color, self.radius + other)

    def __radd__(self, other):
        return self + other


if __name__ == "__main__":
    circle = Circle("red", 5)
    circle2 = Circle("green", 9)

    print(f'circle: {circle}')
    print(f'repr: {circle!r}')

    circle3 = circle + circle2  # same as circle3 = circle.__add__(circle2)
    print(circle3)

    circle4 = circle + 10  # same as circle4 = circle.__add__(10
    print(circle4)

    circle5 = circle2 + circle
    print(circle5)

    circle6 = 10 + circle5

    #  __eq__ = equality
    #  __lt__ = less than
    #  __le__ = less than or equal to
    #  __gt__ = greater than
    #  __ge__ + greater than or equal to
