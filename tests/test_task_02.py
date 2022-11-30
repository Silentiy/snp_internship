import unittest
from task_02 import coincidence


class TaskTwoTestCase(unittest.TestCase):
    def test_empty_input_returns_empty_list(self):
        self.assertEqual(coincidence(), [])

    def test_integers_in_range(self):
        self.assertEqual(coincidence([1, 2, 3, 4, 5], range(3, 6)), [3, 4, 5])

    def test_integers_and_floats_in_range(self):
        self.assertEqual(coincidence([1, 2, 3, 4.4, 5], range(3, 6)), [3, 4.4, 5])

    def test_digits_are_filtered_from_mixed_list_and_found_in_range(self):
        self.assertEqual(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)), [1, 2, 2.5])

    def test_type_error_if_first_argument_is_not_list(self):
        self.assertRaises(TypeError, coincidence, "string", range(2))

    def test_type_error_if_second_argument_is_not_range(self):
        self.assertRaises(TypeError, coincidence, [1, 2, 3, 4.4, 5],122)

    def test_input_list_of_booleans_returns_empty_list(self):
        self.assertEqual(coincidence([True, False], range(12)), [])

    def test_empty_input_list_and_range_returns_empty_list(self):
        self.assertEqual(coincidence([], range(12)), [])


if __name__ == '__main__':
    unittest.main()
