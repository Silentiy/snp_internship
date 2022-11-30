import unittest
from task_01 import is_palindrome


class TaskOneTestCase(unittest.TestCase):
    def test_panama_palindrome(self):
        panama_string = "A man, a plan, a canal -- Panama"
        self.assertEqual(is_palindrome(panama_string), True)

    def test_madam_adam_palindrome(self):
        madam_string = "Madam,   I'm Adam!"
        self.assertEqual(is_palindrome(madam_string), True)

    def test_integer_input_palindrome(self):
        self.assertEqual(is_palindrome(333), True)

    def test_float_input_palindrome(self):
        self.assertEqual(is_palindrome(122.221), True)

    def test_none_input_not_palindrome(self):
        self.assertEqual(is_palindrome(None), False)

    def test_empty_input_palindrome(self):
        self.assertEqual(is_palindrome(), True)

    def test_list_with_boolean_and_strings_input_palindrome(self):
        boolean_strings_list_input = [True, False, "eslaF", "eurT"]
        self.assertEqual(is_palindrome(boolean_strings_list_input), True)

    def test_set_of_strings_input_not_palindrome(self):
        set_of_strings_input = {"a", "b"}
        self.assertEqual(is_palindrome(set_of_strings_input), False)

    def test_set_of_booleans_integer_and_strings_not_palindrome(self):
        messed_input_set = {"a", "b", 22, None, True}
        self.assertEqual(is_palindrome(messed_input_set), False)

    def test_dictionary_input_not_palindrome(self):
        dictionary_input = {"a": 11, "b": 11, "c": 11}
        self.assertEqual(is_palindrome(dictionary_input), False)

    def test_tuple_input_palindrome(self):
        tuple_input = (1, "a", "b", "a", 1)
        self.assertEqual(is_palindrome(tuple_input), True)

    def test_bytes_input_not_palindrome(self):
        bytes_input = bytes(11)
        self.assertEqual(is_palindrome(bytes_input), False)

    def test_range_input_not_palindrome(self):
        range_input = range(1, 12)
        self.assertEqual(is_palindrome(range_input), False)

    def test_abracadabra_string_not_palindrome(self):
        abracadabra_string = "Abracadabra"
        self.assertEqual(is_palindrome(abracadabra_string), False)

    def test_single_unicode_character_palindrome(self):
        unicode_single_character_input = u'\xed'
        self.assertEqual(is_palindrome(unicode_single_character_input), True)


if __name__ == '__main__':
    unittest.main()
