import string


def is_palindrome(string_data: str) -> bool:
    """ Checks if a given string is palindrome.
    Font case, spaces and punctuation are neglected """

    if not type(string_data) in (list, tuple, set, dict, str, bool, int, float):
        raise TypeError("Incorrect data type! Please,"
                        " provide a string for input of the function!")

    if isinstance(string_data, (list, tuple, set)):
        casted_string = " ".join([str(data) for data in string_data])
    elif isinstance(string_data, dict):
        casted_string = " ".join([str(data) for data in string_data.values()])
    else:
        casted_string = str(string_data)

    lower_case_string = casted_string.strip().lower()
    no_punctuation_string = lower_case_string.translate(str.maketrans('', '',
                                                                      string.punctuation))
    clear_string = "".join(no_punctuation_string.split())
    return clear_string[::-1] == clear_string


test_strings = [
    "A man, a plan, a canal -- Panama", "Madam, I'm Adam!",
    333,
    122.221,
    None,
    [True, False, "eslaF", "eurT"],
    {"a", "b"},
    {"a", "b", "a", 22, None, True},
    {"a": 11, "b": 11, "c": 11},
    (1, "a", "b", "a", 1),
    "Abracadabra",
    range(1, 12)
]

if __name__ == "__main__":
    for test_string in test_strings:
        try:
            print(test_string, "# =>", is_palindrome(test_string))
        except Exception as e:
            print(e)
            continue
