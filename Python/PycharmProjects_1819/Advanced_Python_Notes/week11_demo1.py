"""Demo of additional magic methods.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""


class CustomInt(int):
    """A custom integer type for demoing magic methods."""

    def __len__(self):
        """Called when the len operator is used."""
        string_version = str(self)
        return len(string_version)

    def __getitem__(self, item):
        """Called when items are accessed via []s"""
        string_version = str(self)
        character = string_version[item]

        return int(character)

    def __setitem__(self, index, value):
        """Called when items are set via []s"""
        print("calling __setitem__", index, value)


if __name__ == "__main__":
    x = CustomInt(500)
    print("len(x)", len(x))  # the same as print(x.__len__())

    print("x[0]", x[0]) # the same as print(x.__getitem__(0))

    x[1] = 9 # the same as x.__setitem__(0, 9)

