import re
from typing import Union


def multiply_numbers(inputs) -> Union[None, int]:
    """ Finds digits in the given input and returns
    the product of their multiplication.
    If no digits in input were found returns None.
    Function will use values of given dictionaries and
    will unpack numbers from range. In other cases will try
    to get str representation of an object (quits if it failed) """

    if isinstance(inputs, dict):
        line = str(inputs.values())
    elif isinstance(inputs, range):
        line = " ".join([str(num) for num in list(inputs)])
    else:
        try:
            line = str(inputs)
        except Exception as exc:
            print(exc)
            quit()

    numbers = re.findall('[0-9]', line)

    if not numbers:
        return None

    product = 1
    for number in numbers:
        product *= int(number)

    return product


class NoStrReprClass:
    a = 1


no_str_repr = NoStrReprClass()

test_data = [
            None,
            [None, True, False, bytes(2), (1, 2, "b")],
            'ss',
            '1234',
            'sssdd34',
            2.3,
            [5, 6, 4],
            [5, 6, 4, "a", 8],
            [15, 16, 4, "a", 21],
            {"a": 11, "b": 22, "c": 11},
            range(1, 10),
            {no_str_repr, 1}
            ]

if __name__ == "__main__":
    for data in test_data:
        try:
            print(multiply_numbers(data))
        except Exception as e:
            print(e)
            continue
