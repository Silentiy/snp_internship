import unittest
from task_03 import max_odd, unpack_list_into_flat_list, is_odd, is_iterable


class TaskThreeTestCase(unittest.TestCase):

    nested_list = ['ololo', 2, 3, 4, [5, 6, [7, 8, (9, 10, (11, 12)),
                                             {"one": 1, "two": [13, 14, (-15, {16, 17})]}]], None]

    def test_flat_list_from_nested_list_of_different_data_types(self):
        flat_list = ['ololo', 2, 3, 4, None, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, -15, 16, 17]
        self.assertEqual(unpack_list_into_flat_list(self.nested_list), flat_list)

    def test_list_is_iterable(self):
        self.assertEqual(is_iterable([1, 2, 3]), True)

    def test_none_is_not_iterable(self):
        self.assertEqual(is_iterable(None), False)

    def test_17_is_not_odd(self):
        self.assertEqual(is_odd(17), True)

    def test_18_is_odd(self):
        self.assertEqual(is_odd(18), False)

    def test_nested_list_max_odd_17(self):
        self.assertEqual(max_odd(self.nested_list), 17)

    def test_small_nested_list_max_odd_3(self):
        self.assertEqual(max_odd(['ololo', 2, 3, 4, [1, 2], None]), 3)

    def test_list_of_integers_max_odd_3(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 4]), 3)

    def test_list_of_integers_and_floats_max_odd_21(self):
        self.assertEqual(max_odd([21.0, 2, 3, 4, 4]), 21)

    def test_list_of_strings_no_max_odd(self):
        self.assertEqual(max_odd(['ololo', 'fufufu']), None)

    def test_list_of_even_integers_no_max_odd(self):
        self.assertEqual(max_odd([2, 2, 4]), None)

    def test_empty_list_no_max_odd(self):
        self.assertEqual(max_odd([]), None)

    def test_string_input_raises_type_error(self):
        self.assertRaises(TypeError, max_odd, "abracadabra")

    def test_nested_list_with_range_max_odd_9(self):
        self.assertEqual(max_odd([1, 2, 3, range(1, 10, 2)]), 9)

    def test_nested_list_with_tuple_of_booleans_max_odd_3(self):
        self.assertEqual(max_odd([1, 2, 3, (True, False)]), 3)


if __name__ == '__main__':
    unittest.main()

