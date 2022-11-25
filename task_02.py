def coincidence(list_data=None, range_data=None):
    if list_data is None or range_data is None:
        return []

    coincidence_elements = list()
    cleared_list_data = [x for x in list_data if isinstance(x, (int, float)]
    for element in cleared_list_data:
        if min(range_data) <= element <= max(range_data):
            coincidence_elements.append(element)
    return coincidence_elements


def coincidence_2(list_data: list, range_data: range):
    coincidence_elements = list()

    for element in list_data:
        try:
            if min(range_data) <= float(element) <= max(range_data):
                coincidence_elements.append(element)
        except ValueError:
            pass
        except TypeError:
            pass

    return coincidence_elements


test_data = [1, 2, 3, 4, 5]
test_data_2 = [None, 1, 'foo', 4, 2, 2.5]

if __name__ == "__main__":
    print(coincidence_2(test_data_2, range(1, 4)))
