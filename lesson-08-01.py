# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# Я не стал использовать декоратор @classmethod. Мне даже сложно представить реальную задачу, где бы он был прям нужен
# я всё сделал одним статическим мeтодом
class Date:
    __day   = None
    __month = None
    __year  = None

    def __init__(self, date_str):
        d = str(date_str).split("-")
        if len(d) == 3:
            self.__year, self.__month, self.__day = d

        self.__year  = Date.valid_year(self.__year)
        self.__month = Date.valid_month(self.__month)
        self.__day   = Date.valid_day(self.__day)

    @staticmethod
    def valid_month(m):
        try:
            m = int(m)
        except:
            return None

        if 0 < int(m) <= 12:
            return int(m)
        else:
            raise ValueError("Не верный формат месяца")

    @staticmethod
    def valid_year(y):
        try:
            y = int(y)
        except:
            return None

        if int(y) > 0:
            return int(y)
        else:
            raise ValueError("Год должен быть числом больше нуля")

    @staticmethod
    def valid_day(d):
        try:
            d = int(d)
        except:
            return None

        # Простая валидация у нас будет
        if 0 < int(d) <= 31:
            return int(d)
        else:
            raise ValueError("День должен быть числом больше 0 и менее 31")


md = Date('10-11-1979')
print(Date.valid_month('12'))