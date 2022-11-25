def sort_list(list_data: list) -> list:
    if not list_data:
        return []

    sorted_list = list()
    max_number = max(list_data)
    min_number = min(list_data)

    for num in list_data:
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
    [1, 2, 1, 3]
]

if __name__ == "__main__":
    for arr in test_data:
        print(sort_list(arr))
