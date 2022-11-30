import unittest
from task_10 import count_words


class TaskTenTestCase(unittest.TestCase):
    def test_list_input_raises_type_error(self):
        self.assertRaises(TypeError, count_words, ["a", "b", 22])

    def test_integer_input_raises_type_error(self):
        self.assertRaises(TypeError, count_words, 111111)

    def test_string_doo_bee_doo(self):
        self.assertEqual(count_words("Doo bee doo bee doo"), {'doo': 3, 'bee': 2})

    def test_string_man_plan_panama(self):
        self.assertEqual(count_words("A man, a plan, a canal -- Panama"),
                         {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1})


if __name__ == '__main__':
    unittest.main()

