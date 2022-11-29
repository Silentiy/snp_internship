def coincidence(list_data: list = None, range_data: range = None) -> list:
    """ Returns a list of numeric elements from the given list that
     are in the given range """

    if list_data is None or range_data is None:
        return []

    if not isinstance(list_data, list) or not isinstance(range_data, range):
        raise TypeError("First argument should be of 'list'"
                        " type and second of 'range' type!")

    coincidence_elements = list()
    cleared_list_data = [x for x in list_data if type(x) in (int, float)]
    for element in cleared_list_data:
        if min(range_data) <= element <= max(range_data):
            coincidence_elements.append(element)
    return coincidence_elements


test_data = [
    ([1, 2, 3, 4, 5], range(3, 6)),
    ([None, 1, 'foo', 4, 2, 2.5], range(1, 4)),
    ("string", range(2)),
    (None, None),
    ([True, False], 122),
    ([True, False], range(12)),
    ([], range(12))
]

if __name__ == "__main__":
    print(coincidence())
    for data in test_data:
        try:
            print(data, "# =>", coincidence(data[0], data[1]))
        except Exception as e:
            print(e)
            continue

