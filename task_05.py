from datetime import datetime
from datetime import timedelta


def date_in_future(integer: int) -> str:
    """ Returns data in the future after given number of days from now.
     If not positive integer is given as input - returns current data.
     Returned data format is as follows: 'dd-mm-yyyy hh:mm:ss’"""

    now = datetime.now()
    date_format = "%d-%m-%Y %H:%M:%S"

    if type(integer) is int and integer > 0:
        delta = timedelta(days=integer)
        future_date = now + delta
        return future_date.strftime(date_format)
    else:
        return now.strftime(date_format)


test_data = ["a", 1, 2, -5, 11.1, (1, 2), True]

if __name__ == "__main__":
    for num in test_data:
        try:
            print(num, "# =>", date_in_future(num))
        except Exception as e:
            print(e)
            continue
