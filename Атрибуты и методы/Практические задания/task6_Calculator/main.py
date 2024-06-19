from typing import Union

class Calculator:
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]):
        """ Сложение """
        return a + b

    @staticmethod
    def mul(a: Union[int, float], b: Union[int, float]):
        """ Сложение """
        return a * b


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
