from operator import itemgetter
from typing import Dict, Union


def connect_dicts(dict_one: Dict[str, Union[int, float]],
                  dict_two: Dict[str, Union[int, float]]) -> dict:

    if not is_input_valid(dict_one, dict_two):
        return is_input_valid(dict_one, dict_two)

    if sum(dict_one.values()) == sum(dict_two.values()) or \
            sum(dict_one.values()) < sum(dict_two.values()):
        main_dict = dict_two
        second_dict = dict_one
    else:
        main_dict = dict_one
        second_dict = dict_two

    connected_dict = second_dict | main_dict
    filtered_dict = {key: value for key, value in connected_dict.items() if value > 10}
    sorted_dict = dict(sorted(filtered_dict.items(), key=itemgetter(1)))

    return sorted_dict


def is_input_valid(data_one, data_two) -> bool:
    if not isinstance(data_one, dict) or not isinstance(data_two, dict):
        return TypeError("Arguments should be of 'dict' type!")

    if not all([isinstance(value, (int, float)) for value in data_one.values()]) or \
            not all([isinstance(value, (int, float)) for value in data_two.values()]):
        return TypeError("Values in dicts should be of type 'int' or 'float'!")

    if not all([isinstance(key, str) for key in data_one.keys()]) or \
            not all([isinstance(key, str) for key in data_two.keys()]):
        return TypeError("Keys in dicts should be of type 'str'!")

    return True


test_data = [({"a": 2, "b": 12}, {"c": 11, "e": 5}),
             ({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}),
             ({"a": 14, "b": 12}, {"c": 11, "a": 15}),
             ({"a": 14, "b": 12}, {"c": 11, "a": "15"}),
             ({"a": 15, "b": 12}, {"c": 12, "a": 15})
             ]

if __name__ == "__main__":
    for data in test_data:
        try:
            print(connect_dicts(data[0], data[1]))
        except TypeError as e:
            print(e)
            continue

