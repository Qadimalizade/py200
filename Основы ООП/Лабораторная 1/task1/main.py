from typing import Union
class Exchange:
    def __init__(self, rur, acc_balance):# TODO Написать 3 класса с документацией и аннотацией типов
        """
                Создание и подготовка к работе объекта "Обменник"

                :param rur: Российские Рубли зашедшие в обменник
                :param acc_balance: общая сумма после внесени денежных средств

                Примеры:
                >>> day = Exchange(500, 1500) # инициализация экземпляра класса
                """
        if not isinstance(rur, (int, float)):
            raise TypeError("Российские Рубли зашедшие в обменник должен быть типа int или float")
        if not rur > 0:
            raise ValueError("Российские Рубли зашедшие в обменник должен быть положительным числом")
        self.rur = rur

        if not isinstance(acc_balance, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        if acc_balance < 0:
            raise ValueError("Баланс должен быть положительным числом")
        self.acc_balance = acc_balance

    def cash_in_Exchange(self):
        """
        Функция которая проверяет остаток на балансе

        :return: объем денег в кассе

        Примеры:
        >>> day1 = Exchange(1850, 8541535)
        >>> day1.cash_in_Exchange()
        """
        ...

    def extra_money(self):
        """
            Перелимит по кассе после чего вызывается инкассаторы.
            :param acc_balance: Кол-во денег в кассе

            :raise ValueError: Если количество денег превышает допустимую норму, то вызывается ошибка

            Примеры:
            >>> day1 = Exchange(2000, 184740)
            >>> day1.extra_money(50000000000000)
            """
        ...

if __name__ == "__main__":
    day1 = Exchange(15200, 181000)
    print(day1.rur, day1.acc_balance)
    import doctest
    doctest.testmod()