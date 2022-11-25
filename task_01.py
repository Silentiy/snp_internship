import string


def is_palindrome(string_data: str):
    casted_string = str(string_data)
    casted_string = casted_string.lower()
    casted_string = casted_string.strip().translate(str.maketrans('', '', string.punctuation))
    casted_string = "".join(casted_string.split())
    print(casted_string)
    return casted_string[::-1] == casted_string


test_strings = ["A man, a plan, a canal -- Panama", "Madam, I'm Adam!",
                333, None, "Abracadabra"]

if __name__ == "__main__":
    for test_string in test_strings:
        print(test_string, "# =>", is_palindrome(test_string))
