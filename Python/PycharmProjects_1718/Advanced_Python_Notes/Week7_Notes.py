print("hello")

a = 2


class InvalidInputError(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return f"invalid input: {self.value}"


def prompt_user():
    try:
        value = input("enter an integer > ")
        return int(value)
    except ValueError as e:
        raise InvalidInputError(value) from e


def prompt_for_n_values(n):
    return [prompt_user() for _ in range(n)]


try:
    values = prompt_for_n_values(3)
    print(values)
except InvalidInputError as e:
    print("There was problem > ", e)

while True:
    try:
        value = prompt_user()
    except InvalidInputError as e:
        print("Invalid Input", e.value)
    else:
        print(value / 2)
        break



