"""More magic methods and extending built-ins.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

class CustomList(list):
    def __init__(self, *args):
        super().__init__(args)

    def __getitem__(self, item):
        print("Calling __getitem__ with", item)

        # don't do self[item], as this would keep calling this function
        # repeatedly, instead:
        return super().__getitem__(item)

    def __setitem__(self, item, value):
        print("Calling __setitem__ with", item, value)
        super().__setitem__(item, value)


if __name__ == "__main__":
    test = CustomList(1,2,3,4)
    print(test)
    print(test[0])
    test[0] = 5