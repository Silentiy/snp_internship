import unittest
from task_09 import is_input_valid, connect_dicts


class TaskNineTestCase(unittest.TestCase):
    def test_second_argument_not_dict_type_returns_false(self):
        self.assertEqual(is_input_valid({"a": 11, "b": 12}, (13, 14)), False)

    def test_not_all_values_in_dict_are_of_int_type_returns_false(self):
        self.assertEqual(is_input_valid({"a": 14, "b": 12}, {"c": 11, "a": "15"}), False)

    def test_not_all_keys_in_dict_are_of_str_type_returns_false(self):
        self.assertEqual(is_input_valid({("a", ): 2, "b": 12}, {"c": 11, "e": 5}), False)

    def test_values_less_than_ten_are_filtered(self):
        self.assertEqual(connect_dicts({"a": 2, "b": 1}, {"c": 1, "e": 5}), {})

    def test_second_dict_keys_get_priority_when_sum_of_values_same(self):
        self.assertEqual(connect_dicts({'a': 14, 'b': 12}, {'c': 11, 'a': 15}),
                         {'c': 11, 'b': 12, 'a': 15})

    def test_first_dict_keys_get_priority_when_sum_of_first_dict_values_bigger(self):
        self.assertEqual(connect_dicts({'a': 13, 'b': 9, 'd': 11}, {'c': 12, 'a': 15}),
                         {'d': 11, 'c': 12, 'a': 13})

    def test_several_keys_with_same_value_sorts_proceeding(self):
        self.assertEqual(connect_dicts({"a": 15, "b": 12}, {"c": 12, "a": 15}),
                         {'b': 12, 'c': 12, 'a': 15})

    def test_usual_use_case_one(self):
        self.assertEqual(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}),
                         {'c': 11, 'b': 12})

    def test_usual_use_case_two(self):
        self.assertEqual(connect_dicts({"a": 10, "b": 9}, {"c": 9, "a": 15}),
                         {'a': 15})

if __name__ == '__main__':
    unittest.main()
