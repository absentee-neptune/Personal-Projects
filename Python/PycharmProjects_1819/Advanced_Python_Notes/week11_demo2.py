"""Demo of advanced function usage.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""


def do_something(value1, value2, value3=3):
    print(value1, value2, value3)


def do_something_else(a, b, *values, c=None, **kwargs):
    print(values)
    print(kwargs)


def add_10(x):
    return x + 10


def use_function(function, value):
    return function(value)


def create_add_x(x):
    def add_x(value):
        return value + x
    return add_x


def wrap_tag(tag):
    def wrapper(contents):
        return f"<{tag}>{contents}</{tag}>"

    return wrapper


if __name__ == "__main__":
    values = [10, 20, 30]
    do_something(*values) # the same as do_something(values[0], values[1], values[2])

    values2 = [100, 200]
    do_something(*values2)

    do_something_else(1,2,3,4,5,"a", c=45, d=100, e=99)

    add_30 = create_add_x(30)
    print(add_30(20))


    make_h1 = wrap_tag("h1")
    print(make_h1("This is a header"))
    print(make_h1("Another header"))

    make_p = wrap_tag("p")
    print(make_p("The first paragraph of my website."))
