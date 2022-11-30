import unittest
from task_08 import multiply_numbers, BadStrReprClass


class TaskEightTestCase(unittest.TestCase):
    def test_empty_input_returns_none(self):
        self.assertEqual(multiply_numbers(), None)

    def test_none_input_returns_none(self):
        self.assertEqual(multiply_numbers(None), None)

    def test_list_with_messed_data_type_input_returns_2(self):
        self.assertEqual(multiply_numbers([None, True, False, (1, 2, "b")]), 2)

    def test_list_with_messed_data_type_and_bytes_input_returns_0(self):
        self.assertEqual(multiply_numbers([None, True, False, bytes(2), (1, 2, "b")]), 0)

    def test_string_input_without_digits_returns_none(self):
        self.assertEqual(multiply_numbers('ss'), None)

    def test_string_input_with_digits_returns_24(self):
        self.assertEqual(multiply_numbers('1234'), 24)

    def test_string_input_with_digits_and_letters_returns_12(self):
        self.assertEqual(multiply_numbers('sssdd34'), 12)

    def test_float_input_returns_6(self):
        self.assertEqual(multiply_numbers(2.3), 6)

    def test_list_of_integers_input_returns_120(self):
        self.assertEqual(multiply_numbers([5, 6, 4]), 120)

    def test_list_of_integers_and_floats_input_returns_120(self):
        self.assertEqual(multiply_numbers([5, 6.4]), 120)

    def test_list_of_integers_and_strings_input_returns_80(self):
        self.assertEqual(multiply_numbers([5, "a", 8, "2"]), 80)

    def test_dict_input_returns_4(self):
        self.assertEqual(multiply_numbers({"a": 11, "b": 22, "c": 11}), 4)

    def test_range_input_returns_362880(self):
        self.assertEqual(multiply_numbers(range(1, 10)), 362880)

    def test_list_with_broken_str_method_data_raises_exception(self):
        no_str_repr = BadStrReprClass()
        self.assertRaises(SystemExit, multiply_numbers, {no_str_repr, 1})


if __name__ == '__main__':
    unittest.main()

