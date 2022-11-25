import re
from typing import Union


def multiply_numbers(inputs) -> Union[None, int]:
    if isinstance(inputs, (list, tuple, set)):
        line = " ".join(str(inputs))
    elif isinstance(inputs, dict):
        line = " ".join(str(inputs.values()))
    else:
        line = str(inputs)

    numbers = re.findall('[0-9]', line)
    if not numbers:
        return None

    product = 1

    for number in numbers:
        product *= int(number)

    return product


test_data = [
            None,
            'ss',
            '1234',
            'sssdd34',
            2.3,
            [5, 6, 4],
            [5, 6, 4, "a", 8]
            ]

if __name__ == "__main__":
    for data in test_data:
        print(multiply_numbers(data))
