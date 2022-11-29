from collections import deque
from typing import Union


def max_odd(array: list) -> Union[int, float, None]:
    """ Returns maximum odd number in the given list (if any)
    Otherwise returns None """

    if not isinstance(array, list):
        raise TypeError("Please, provide a data of 'list' type for input!")

    if not array:
        return None

    flat_array = unpack_list_into_flat_list(array)

    odd_numbers = [x for x in flat_array if type(x) in (float, int) and is_odd(x)]

    if not odd_numbers:
        return None
    return max(odd_numbers)


def unpack_list_into_flat_list(list_data: list) -> list:
    """ 'Unpacks' given list i.e. grabs nested elements
     and appends their atomic values into resulting list.
     Supports only 'list', 'tuple', 'set', 'dict', 'str',
     'bool', 'int', 'float' and 'range' data types and ignores others """

    unpacked = list()
    to_unpack = deque()
    to_unpack += list_data

    while to_unpack:
        element = to_unpack.popleft()
        if not type(element) in (list, tuple, set, dict, str, bool, int, float, range):
            continue
        if isinstance(element, (list, tuple, set)):
            for elem in element:
                to_unpack.append(elem)
        elif isinstance(element,  dict):
            for key, value in element.items():
                to_unpack.append(value)
        elif isinstance(element, range):
            to_unpack.append(list(element))
        else:
            unpacked.append(element)
    return unpacked


def is_odd(number: Union[int, float]) -> bool:
    return number % 2 != 0


test_data = [
    ['ololo', 2, 3, 4, [5, 6, [7, 8, (9, 10, (11, 12)),
                               {"one": 1, "two": [13, 14, (-15, {16, 17})]}]], None],
    [1, 2, 3, 4, 4],
    [21.0, 2, 3, 4, 4],
    ['ololo', 2, 3, 4, [1, 2], None],
    ['ololo', 'fufufu'],
    [2, 2, 4],
    [],
    "abracadabra",
    [1, 2, 3, range(1, 10, 2)],
    [1, 2, 3, (True, False)],
    [True, False]
    ]

if __name__ == "__main__":
    for arr in test_data:
        try:
            print(arr, "# =>", max_odd(arr))
        except Exception as e:
            print(e)
            continue
