import unittest
from task_11 import Dessert


class MyTestCase(unittest.TestCase):
    def test_setters_and_getters_work(self):
        des = Dessert()
        des.name = "icecream"
        des.calories = 199
        self.assertEqual([des.name, des.calories], ["icecream", 199])

    def test_constructor_and_getters_work(self):
        des_2 = Dessert("cheesecake", 202)
        self.assertEqual([des_2.name, des_2.calories], ["cheesecake", 202])

    def test_is_delicious_method_works(self):
        des_2 = Dessert("cheesecake", 202)
        self.assertEqual(des_2.is_delicious(), True)

    def test_is_healthy_method_works(self):
        des_2 = Dessert("cheesecake", 202)
        self.assertEqual(des_2.is_healthy(), False)

    def test_str_method_works(self):
        des_2 = Dessert("cheesecake", 202)
        self.assertEqual(str(des_2), "Dessert 'cheesecake' has '202' calories in it.")

    def test__is_name_of_type_string(self):
        des = Dessert()
        self.assertEqual(des._Dessert__is_name_of_type_string(1), False)

    def test__is_calories_of_type_int(self):
        des = Dessert()
        self.assertEqual(des._Dessert__is_calories_of_type_int_or_float(1), True)

    def test__is_calories_greater_zero_true(self):
        des = Dessert()
        self.assertEqual(des._Dessert__is_calories_greater_zero(1), True)

    def test__is_calories_greater_zero_false(self):
        des = Dessert()
        self.assertEqual(des._Dessert__is_calories_greater_zero(-1), False)

if __name__ == '__main__':
    unittest.main()
