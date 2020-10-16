"""Demo of attr magic methods.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

class Demo:

    def __getattr__(self, item):
        print("Calling __getattr__ ", item)
        return 42

    def __setattr__(self, key, value):
        print("Calling __setattr__ ", key, value)

    def __delattr__(self, item):
        print("Calling __delattr__", item)

if __name__ == "__main__":
    demo = Demo()

    print(demo.something)

    demo.something = 42

    del demo.something
