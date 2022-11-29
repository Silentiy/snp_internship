from operator import itemgetter
from typing import Dict, Union


def connect_dicts(dict_one: Dict[str, Union[int, float]],
                  dict_two: Dict[str, Union[int, float]]) -> Union[dict, str]:
    """ Connects two given dicts using the following rules:
    - keys of a dict that has bigger sum of its values have priority;
    - if both dicts have equal sum of their values, second dict keys' get priority;
    - keys with corresponding values lesser than 10 are neglected;
    - resulting dict returns being sorted by its' values.
    Keys of the input dicts have to be of 'str' type and values of 'int' or 'float' type.
    If other types are given as keys and/or values,
    returns 'Invalid input' message """

    if not is_input_valid(dict_one, dict_two):
        return "Invalid input!"

    if sum(dict_one.values()) == sum(dict_two.values()) or \
            sum(dict_one.values()) < sum(dict_two.values()):
        main_dict = dict_two
        second_dict = dict_one
    else:
        main_dict = dict_one
        second_dict = dict_two

    connected_dict = second_dict | main_dict
    filtered_dict = {key: value for key, value in connected_dict.items() if value >= 10}
    sorted_dict = dict(sorted(filtered_dict.items(), key=itemgetter(1)))

    return sorted_dict


def is_input_valid(data_one, data_two) -> bool:
    """ Checks if data given to 'connect_dicts' function is of 'dict' type with
    keys of 'str' type and values of 'int' or 'float' type """

    if not isinstance(data_one, dict) or not isinstance(data_two, dict):
        return False

    if not all([True if type(value) in (int, float) else False
                for value in data_one.values()]) or \
            not all([True if type(value) in (int, float) else False
                     for value in data_two.values()]):
        return False

    if not all([isinstance(key, str) for key in data_one.keys()]) or \
            not all([isinstance(key, str) for key in data_two.keys()]):
        return False

    return True


test_data = [
    ({"a": 11, "b": 12}, (13, 14)),
    ({"a": 14, "b": 12}, {"c": 11, "a": "15"}),
    ({("a", ): 2, "b": 12}, {"c": 11, "e": 5}),
    ({"a": 2, "b": 12}, {"c": 11, "e": 5}),
    ({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}),
    ({"a": 14, "b": 12}, {"c": 11, "a": 15}),
    ({"a": 15, "b": 12}, {"c": 12, "a": 15}),
    ({"a": 10, "b": 9}, {"c": 9, "a": 15})
]

if __name__ == "__main__":
    for data in test_data:
        try:
            print(data, "# =>", connect_dicts(data[0], data[1]))
        except TypeError as e:
            print(e)
            continue
