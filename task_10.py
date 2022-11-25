import string


def count_words(string_data: str) -> dict:
    if not isinstance(string_data, str):
        raise ValueError("You have to provide string as input!")

    histogram = dict()
    cleared_string = string_data.strip().lower().translate(str.maketrans('', '', string.punctuation))
    words = cleared_string.split()

    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram


test_data = [
    "A man, a plan, a canal -- Panama",
    "Doo bee doo bee doo"
    ]

if __name__ == "__main__":
    for test_string in test_data:
        print(count_words(test_string))
