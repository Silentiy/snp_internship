import unittest
from task_04 import sort_list


class TaskFourTestCase(unittest.TestCase):
    def test_empty_input_list_empty_output_list(self):
        self.assertEqual(sort_list([]), [])

    def test_one_integer_input_list_doubled_integer_output_list(self):
        self.assertEqual(sort_list([1]), [1, 1])

    def test_positive_even_integers_list(self):
        self.assertEqual(sort_list([2, 4, 6, 8]), [8, 4, 6, 2, 2])

    def test_positive_and_negative_even_and_odd_integers_list(self):
        self.assertEqual(sort_list([1, 2, -5, 1, 3, -4.99, 8, 12]),
                         [1, 2, 12, 1, 3, 8, -5, -5])

    def test_positive_even_and_odd_integers_list(self):
        self.assertEqual(sort_list([1, 2, 1, 3]), [3, 2, 3, 1, 1])

    def test_non_list_input_raises_type_error(self):
        self.assertRaises(TypeError, sort_list, True)

    def test_input_list_with_messed_data_types(self):
        self.assertEqual(sort_list(["a", None, False, range(5), 1.1, 12, 1.1, 12]), [12, 12, 12])


if __name__ == '__main__':
    unittest.main()
