import string
from typing import List


def combine_anagrams(words_array: List[str]) -> List[List[str]]:
    """ Returns list with groups (lists) of anagrams (if any) for every word
    in the original list. If no anagrams for a word - returns group (list)
    containing solely this word. Neglects font case, punctuation and digits """

    # data sanity check
    if not isinstance(words_array, list):
        raise TypeError("Please, provide a list for an input!")

    if not all([isinstance(word, str) for word in words_array]):
        raise TypeError("Every element of the given list has to be of 'str' type!")

    BANNED_WORDS = [" ", "", ]

    anagrams_result = list()
    words_dict = dict()
    cleaned_words = list()

    # little clean up
    for word in words_array:
        word = word.lower().strip().translate(str.maketrans('', '',
                                                            string.punctuation))
        word = word.translate(str.maketrans('', '', string.digits))
        single_words = word.split()
        word = " ".join(single_words)
        if word not in BANNED_WORDS:
            cleaned_words.append(word)
    # delete duplicates
    cleaned_words = list(dict.fromkeys(cleaned_words))

    # letters histograms for every given word
    for word in cleaned_words:
        words_dict[word] = {}
        for letter in word:
            if letter == " ":  # we will not count whitespaces
                continue
            words_dict[word][letter] = words_dict[word].get(letter, 0) + 1

    # combine anagrams
    while cleaned_words:
        combined_anagrams = list()
        main_word = cleaned_words.pop(0)
        main_histogram = words_dict[main_word]
        for word, histogram in words_dict.items():
            if main_histogram == histogram:  # same number of the same letters
                combined_anagrams.append(word)
                try:
                    cleaned_words.remove(word)
                except ValueError:
                    pass
        anagrams_result.append(combined_anagrams)

    return anagrams_result


test_data = [["cars, ", "for", "for", "for", " potatoes!", "racs?", "four", "scar",
              "creams11", "scream", "carcass"],
             ["a Gentleman  ", "bicycle", "twelve plus one", " ", "vile",
              "elegant  Man", "evil", "New    Year", "villain",
              "eleven plus two", "ubiquitous", "home"],
             ["forty five", "computer", "restful", "desc", "Santa",
              "fluster", "Python", "teacher", "funeral", "scraper",
              "adultery", "cheater", "true lady", "over fifty",
              "satan", "real fun", "Ladybug", "22", " "],
             ["list", 1, "with", True, "bad", None, "data", 11.1]
             ]

if __name__ == "__main__":
    for data in test_data:
        try:
            print(data, "# => \n", combine_anagrams(data))
        except Exception as e:
            print(e)
            continue
