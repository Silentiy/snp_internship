from datetime import datetime
from datetime import timedelta
from typing import Union


def date_in_future(integer) -> datetime:
    now = datetime.now()
    if isinstance(integer, int):
        delta = timedelta(days=integer)
        future_date = now + delta
        return future_date.replace(microsecond=0)
    else:
        return now.replace(microsecond=0)


test_data = ["a", 1, 2]

if __name__ == "__main__":
    for num in test_data:
        print(date_in_future(num))
