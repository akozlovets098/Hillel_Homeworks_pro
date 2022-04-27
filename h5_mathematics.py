from typing import Union

class Calculator:
    def add(self, first_arg:Union[int, float], second_arg:Union[int, float]):
        pass


class IntegerCalculator(Calculator):
    def add(self, first_arg: Union[int, float], second_arg: Union[int, float]) -> int:
        return int(round(first_arg + second_arg, 0))


class FloatCalculator(Calculator):
    def add(self, first_arg: Union[int, float], second_arg: Union[int, float]) -> float:
        return float(first_arg + second_arg)


def make_add(calc_obj: Union[IntegerCalculator, FloatCalculator], first_arg: Union[int, float], second_arg: Union[int, float]) -> Union[int, float]:
    return calc_obj.add(first_arg, second_arg)


if __name__ == '__main__':
    int_obj = IntegerCalculator()
    float_obj = FloatCalculator()
    print(make_add(int_obj, 2.4, 3))
    print(make_add(float_obj, 2.5, 3))
