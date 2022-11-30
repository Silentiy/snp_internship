import unittest
from task_07 import combine_anagrams


class TaskSevenTestCase(unittest.TestCase):
    standard_answer = [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream'], ['carcass']]

    def test_duplicates_are_filtered(self):
        list_with_duplicates = ["cars", "cars", "for", "for", "for", "potatoes", "potatoes",
                                "racs", "racs", "racs", "four", "four", "scar", "scar",
                                "creams", "scream", "carcass", "creams", "scream", "carcass"
                                ]
        self.assertEqual(combine_anagrams(list_with_duplicates), self.standard_answer)

    def test_extra_spaces_numbers_punctuation_are_filtered(self):
        list_with_punctuation_and_numbers = ["cars, ", "for", "for", "for", " potatoes!",
                                             "racs?", "four", "scar", "creams11", "scream", "carcass"
                                             ]
        self.assertEqual(combine_anagrams(list_with_punctuation_and_numbers), self.standard_answer)

    def test_empty_strings_are_filtered(self):
        list_with_empty_strings = ["cars", "for", "potatoes", " ",
                                   "racs", "four", "scar", "creams", "scream", "carcass"
                                   ]
        self.assertEqual(combine_anagrams(list_with_empty_strings), self.standard_answer)

    def test_list_with_messed_data_types_raises_type_error(self):
        list_with_messed_data = ["cars", 1, "for", "potatoes", " ",
                                 "racs", "four", "scar", True, "creams", None,
                                 "scream", "carcass", 11.1, range(2)
                                 ]
        self.assertRaises(TypeError, combine_anagrams, list_with_messed_data)

    def test_non_list_input_raises_type_error(self):
        self.assertRaises(TypeError, combine_anagrams, "string")

    def test_list_with_multi_words_data(self):
        list_with_phrases_strings = ["a Gentleman  ", "bicycle", "twelve plus one", "vile",
                                     "elegant  Man", "evil", "New Year", "villain",
                                     "eleven plus two", "ubiquitous", "home"]
        answer = [['a gentleman', 'elegant man'], ['bicycle'], ['twelve plus one', 'eleven plus two'],
                  ['vile', 'evil'], ['new year'], ['villain'], ['ubiquitous'], ['home']]
        self.assertEqual(combine_anagrams(list_with_phrases_strings), answer)


if __name__ == '__main__':
    unittest.main()
