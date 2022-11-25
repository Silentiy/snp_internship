from collections import deque
from typing import Union


def max_odd(array: list) -> Union[int, float, None]:
    if not array:
        return None

    flat_array = unpack(array)

    odd_numbers = [x for x in flat_array if isinstance(x, (float, int)) and is_odd(x)]

    if not odd_numbers:
        return None
    return max(odd_numbers)


def unpack(list_data: list) -> list:
    unpacked = list()
    to_unpack = deque()
    to_unpack += list_data

    while to_unpack:
        element = to_unpack.popleft()
        if isinstance(element, (list, tuple)):
            for elem in element:
                to_unpack.append(elem)
        elif isinstance(element,  dict):
            for key, value in element.items():
                to_unpack.append(value)
        else:
            unpacked.append(element)
    return unpacked


def is_odd(number: Union[int, float]) -> bool:
    return number % 2 != 0


test_data = [
    ['ololo', 2, 3, 4, [5, 6, [7, 8, (9, 10, (11, 12)), {"one": 1, "two": [13, 14, (-15, 16)]}]], None],
    [1, 2, 3, 4, 4],
    [21.0, 2, 3, 4, 4],
    ['ololo', 2, 3, 4, [1, 2], None],
    ['ololo', 'fufufu'],
    [2, 2, 4],
    []
    ]

if __name__ == "__main__":
    for arr in test_data:
        print(max_odd(arr))
