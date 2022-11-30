import unittest
from datetime import datetime, timedelta
from task_05 import date_in_future


class TaskFiveTestCase(unittest.TestCase):
    date_format = "%d-%m-%Y %H:%M:%S"

    def get_current_date_and_time(self):
        return datetime.now().strftime(self.date_format)

    def test_string_input_returns_current_date(self):
        self.assertEqual(date_in_future("a"), self.get_current_date_and_time())

    def test_negative_integer_input_returns_current_date(self):
        self.assertEqual(date_in_future(-5), self.get_current_date_and_time())

    def test_float_input_returns_current_date(self):
        self.assertEqual(date_in_future(11.1), self.get_current_date_and_time())

    def test_boolean_input_returns_current_date(self):
        self.assertEqual(date_in_future(True), self.get_current_date_and_time())

    def test_tuple_input_returns_current_date(self):
        self.assertEqual(date_in_future((1, 2)), self.get_current_date_and_time())

    def test_one_day_into_future(self):
        delta = timedelta(1)
        future_date = datetime.now() + delta
        self.assertEqual(date_in_future(1), future_date.strftime(self.date_format))

    def test_hundred_days_into_future(self):
        delta = timedelta(100)
        future_date = datetime.now() + delta
        self.assertEqual(date_in_future(100), future_date.strftime(self.date_format))


if __name__ == '__main__':
    unittest.main()
