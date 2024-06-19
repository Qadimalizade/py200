from datetime import datetime


class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if (year % 4) == 0:
            if (year % 100) == 0 and year % 400 == 0:
                return True
            else:
                return False
        return False

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if cls.is_leap_year(year) is True:
            return cls.DAY_OF_MONTH[1][month - 1]
        else:
            return cls.DAY_OF_MONTH[0][month - 1]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        try:
            check_date = datetime.fromisoformat(f"{year}-{month:02}-{day:02}")
            return True
        except ValueError:
            return False




if __name__ == "__main__":
    print(Date.is_leap_year(2000))
    print(Date.get_max_day(2,1994))
    print(Date.is_valid_date(30, 8, 1995))
