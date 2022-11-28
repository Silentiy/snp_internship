from typing import List


def sort_list(list_data: List[int]) -> List[int]:
    """ In the given list of integers changes min values to max values and vise versa.
     Filters list from data of any type except integer if provided input is messed """

    if not isinstance(list_data, list):
        raise TypeError("Please, provide a data of 'list' type for input!")

    if not list_data:
        return []

    numbers_list = [x for x in list_data if type(x) in (int, )]

    sorted_list = list()
    max_number = max(numbers_list)
    min_number = min(numbers_list)

    for num in numbers_list:
        if num == max_number:
            sorted_list.append(min_number)
        elif num == min_number:
            sorted_list.append(max_number)
        else:
            sorted_list.append(num)
    sorted_list.append(min_number)

    return sorted_list


test_data = [
    [],
    [2, 4, 6, 8],
    [1],
    [1, 2, 1, 3],
    True,
    ["a", True, False, 11, 12, 11, 12],
    ["a", None, False, range(5), 1.1, 12, 1.1, 12]
]

if __name__ == "__main__":
    for arr in test_data:
        try:
            print(sort_list(arr))
        except Exception as e:
            print(e)
            continue
