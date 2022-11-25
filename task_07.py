# May the dicts be with us (C)
from typing import List


def combine_anagrams(words_array: List[str]) -> List[List[str]]:
    anagrams_result = list()
    words_dict = dict()
    banned_words = [" "]
    cleaned_words = list()

    # little clean up
    for word in words_array:
        if word not in banned_words:
            word = word.lower().strip()
            single_words = word.split()
            word = " ".join(single_words)
            cleaned_words.append(word)
    cleaned_words = list(dict.fromkeys(cleaned_words))

    # letters histograms for every given word
    for word in cleaned_words:
        words_dict[word] = {}
        for letter in word:
            if letter == " ":  # we will not count whitespaces
                continue
            words_dict[word][letter] = words_dict[word].get(letter, 0) + 1

    # combine anagrams (pop items directly from words_dict?)
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


test_data = [["cars ", "for", "for", "for", " potatoes", "racs", "four", "scar",
              "creams", "scream", "carcass"],
             ["a Gentleman  ", "bicycle", "twelve plus one", " ", "vile",
              "elegant  Man", "evil", "New    Year", "villain",
              "eleven plus two", "ubiquitous", "home"],
             ["forty five", "computer", "restful", "desc", "Santa",
              "fluster", "Python", "teacher",  "funeral", "scraper",
              "adultery", "cheater", "true lady", "over fifty",
              "satan", "real fun", "Ladybug"]
             ]

if __name__ == "__main__":
    for data in test_data:
        print(combine_anagrams(data))
