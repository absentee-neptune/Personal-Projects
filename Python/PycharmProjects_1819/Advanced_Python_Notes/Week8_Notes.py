'''

class Color:
    def __init__(self, rgb_value, name):
        self._attributes = [rgb_value, name]

    def get_rgb_value(self):
        return self._attributes[0]

    def set_rgb_value(self, rgb_value):
        if len(rgb_value) != 7:
            raise ValueError("rgb_value must be 7 characters")
        if rgb_value[0] != '#':
            raise ValueError("rgb_value must start with #")
        self._attributes[0] = rgb_value

    def get_name(self):
        return self._attributes[1]

    def set_name(self, name):
        self._attributes[1] = name


# More Pythonic Way


class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    @property
    def rgb_value(self):
        return self._rgb_value

    @rgb_value.setter
    def rgb_value(self, rgb_value):
        if len(rgb_value) != 7:
            raise ValueError("rgb_value must be 7 characters")
        if rgb_value[0] != '#':
            raise ValueError("rgb_value must start with #")
        self._rgb_value = rgb_value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


if __name__ == "__main__":
    c = Color('#ff0000', 'bright red')
    c.rgb_value = 'dhdhdhd'
    c.name = 'red'
    print(c.name, c.rgb_value)
'''


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        if len(full_name.split()) != 2:
            raise ValueError("full_name mist contain exactly 2 names")
        self.first_name, self.last_name = full_name.split()


if __name__ == "__main__":
    john = Person('John', "Smith")
    john.first_name = 'Bob'
    print(john.full_name)

    john.full_name = 'Tom Johnson'
    print(john.first_name, john.last_name)