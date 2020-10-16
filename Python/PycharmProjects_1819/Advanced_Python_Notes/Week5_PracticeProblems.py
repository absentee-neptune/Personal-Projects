class Shape:
    def __init__(self, color):
        self.color = color

    def get_area(self):
        return None


class Circle:
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius


class Rectangle:
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width


def main():
    """Simple tests for Shape, Circle, and Rectangle classes."""
    shape = Shape("blue")
    circle = Circle(2.5, "red")
    rectangle = Rectangle(3.5, 10.0, "green")

    print(f"A {shape.color} generic shape has area {shape.get_area()}")
    print(f"A {circle.color} circle with radius {circle.radius} "
          f" has area {circle.get_area():.4f}")

    print(f"A {rectangle.color} rectangle with length {rectangle.length} and "
          f"width {rectangle.width} has area {rectangle.get_area():.4f}")


if __name__ == "__main__":
    main()
