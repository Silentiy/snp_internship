import unittest
from task_12 import JellyBean


class MyTestCase(unittest.TestCase):
    def test_initialization_and_getters_work(self):
        j_bean = JellyBean("jelly bean", 200, "pistachio")
        self.assertEqual([j_bean.name, j_bean.calories, j_bean.flavor],
                         ["jelly bean", 200, "pistachio"])

    def test_setters_and_getters_work(self):
        j_bean_licorice = JellyBean()
        j_bean_licorice.name = "jelly bean licorice"
        j_bean_licorice.calories = 201
        j_bean_licorice.flavor = "black licorice"
        self.assertEqual([j_bean_licorice.name, j_bean_licorice.calories, j_bean_licorice.flavor],
                         ["jelly bean licorice", 201, "black licorice"])

    def test_not_black_licorice_is_delicious(self):
        j_bean = JellyBean("jelly bean", 200, "pistachio")
        self.assertEqual( j_bean.is_delicious(), True)

    def test_black_licorice_is_not_delicious(self):
        j_bean = JellyBean("jelly bean", 200, "black licorice")
        self.assertEqual( j_bean.is_delicious(), False)


if __name__ == '__main__':
    unittest.main()
