class Dessert:
    """ Class for storing dessert's name and calories
     Has methods to check whether dessert is delicious and healthy """

    _CALORIES_LIMIT = 200

    __slots__ = ["__name", "__calories"]

    def __init__(self, name="dessert_name", calories=0):
        self.name = name
        self.calories = calories

    @staticmethod
    def __is_name_of_type_string(name):
        return isinstance(name, str)

    @staticmethod
    def __is_calories_of_type_int_or_float(calories):
        return type(calories) in (int, float)

    @staticmethod
    def __is_calories_greater_zero(calories):
        return calories >= 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not Dessert.__is_name_of_type_string(name):
            raise ValueError("Invalid input: 'str' type should be given for name")
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        if not Dessert.__is_calories_of_type_int_or_float(calories):
            raise ValueError("Invalid input: 'int' or 'float' type should be given for calories")
        if not Dessert.__is_calories_greater_zero(calories):
            raise ValueError("Calories can not be lesser, than 0")
        self.__calories = calories

    def is_healthy(self):
        return self.calories < Dessert._CALORIES_LIMIT

    def is_delicious(self):
        return True

    def __str__(self):
        return f"Dessert '{self.name}' has '{self.calories}' calories in it"


if __name__ == "__main__":
    des = Dessert()
    des.name = "icecream"
    des.calories = 199
    des_2 = Dessert("cream", 202)

    print(des.name, des.calories)
    print(des.name, des.calories, des_2, des_2.is_healthy(), des_2.is_delicious())
