# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f"MyClass instance with value {self.value}"
#
#     def __lt__(self, other):
#         print("in __lt__")
#         return self.value < other
#         # or
#         # return self.value > other  # other.__gt__(self.value)
#
#     def __gt__(self, other):
#         print("in __gt__")
#         return self.value > other
#         # or
#         # return self.value < other  # other.__lt__(self.value)
#
#
# if __name__ == "__main__":
#     obj1 = MyClass(15)
#     obj2 = MyClass("hello")
#     print(obj1 < obj2)  # this is the same as print(obj1.__lt__(obj2)
#     print(obj1 > obj2)  # this is the same as print(obj1.__gt__(obj2)
#     print(obj1 < 20)


# def print_repeatedly(thing, *args, n=1, **kwargs):
#     for _ in range(n):
#         print(thing, *args, **kwargs)
#
#
# if __name__ == "__main__":
#     print_repeatedly('hello', 'world', 'ok', 'more words', n=10, sep="+", end="\n\n\n")


def print_count(*args):
    print(len(args))


def do_repeatedly(function, *args, n=1, **kwargs):
    for _ in range(n):
        function(*args, **kwargs)


def square(x):
    return x**2


def cube(x):
    return x**3


def apply_to_all(function, values):
    return [function(value) for value in values]


if __name__ == "__main__":
    # do_repeatedly(print_count, 'hello', 'world', n=3)
    print(apply_to_all(lambda x: x**2, [1, 2, 3]))
