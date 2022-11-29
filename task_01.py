import string


def is_palindrome(string_data: str) -> bool:
    """ Casts given data into a string using str() method
     (quits execution if error). Checks if the string is a palindrome.
     Font case, spaces and punctuation are neglected """

    try:
        casted_string = str(string_data)
    except Exception as exc:
        print(exc)
        quit()

    lower_case_string = casted_string.strip().lower()
    no_punctuation_string = lower_case_string.translate(str.maketrans('', '',
                                                                      string.punctuation))
    clear_string = "".join(no_punctuation_string.split())
    return clear_string[::-1] == clear_string


test_strings = [
    "A man, a plan, a canal -- Panama",
    "Madam,   I'm Adam!",
    333,
    122.221,
    None,
    [True, False, "eslaF", "eurT"],
    {"a", "b"},
    {"a", "b", 22, None, True},
    {"a": 11, "b": 11, "c": 11},
    (1, "a", "b", "a", 1),
    "Abracadabra",
    bytes(11),
    range(1, 12),
    u'\xed'
]

if __name__ == "__main__":
    for test_string in test_strings:
        try:
            print(test_string, "# =>", is_palindrome(test_string))
        except Exception as e:
            print(e)
            continue
