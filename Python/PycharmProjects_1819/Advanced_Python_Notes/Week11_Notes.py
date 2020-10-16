class SillyLength:
    def __len__(self):
        return 42


class CustomInt(int):
    def __len__(self):
        return len(str(self))

    def __getitem__(self, item):
        return str(self)[item]

        # or
        # string_version = str(self)
        # character = string_version[item]
        # return int(character)


# if __name__ == "__main__":
    # print(len("hello"))  # string
    # print(len((1, 2, 3, 4)))  # tuple
    #
    # # dictionary
    # my_dict = {"a": 24, "b": 42}
    # print(len(my_dict))
    # print(my_dict["a"])
    #
    # # list
    # my_list = ([1, 2, 3, 4, 1, 2, 3])
    # my_list.append(5)
    # print(len(my_list))
    # print(my_list)
    #
    # # set (for finding unique values)
    # my_set = set([10, 1, 2, 3, 4, 1, 2, 3, 1, 1, 1, 1])
    # my_set.add(5)
    # print(len(my_set))
    # print(my_set)
    # print(5 in my_set)

    # obj = SillyLength()
    # print(len(obj))
    #
    # x = CustomInt(500)
    # print(x)
    # print(len(x))
    # print(x[0])  # the same as print (x.__getitem__(0))

# --------------------------------------------------------


def do_something(value1, value2, value3=3):
    print(value1, value2, value3)


def do_something_else(values_list):
    print(*values_list)


if __name__ == "__main__":
    values = [10, 20, 30]
    # do_something(*values)  # the same as do_something(values[0], values[1], values[2])

    values2 = [100, 200]
    # do_something(*values2)

    do_something_else(values)
