# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum():
    __real = None
    __imaginary = None

    @property
    def real(self):
        return self.__real

    @property
    def imaginary(self):
        return self.__imaginary


    def __init__(self, r, i):
        self.__real = int(r)
        self.__imaginary = int(i)

    def __str__(self):
        return f"{self.real}{'+' if self.imaginary>0 else ''}{self.imaginary}i"

    def __add__(self, other):
        if type(other) == ComplexNum:
            return ComplexNum(self.real+other.real, self.imaginary+other.imaginary)
        else:
            raise ValueError("Комплексные числа могу складывать только между собой")

    def __mul__(self, other):
        if type(other) == ComplexNum:
            r = self.real*other.real + self.imaginary*other.imaginary*(-1)
            i = self.real*other.imaginary + self.imaginary*other.real
            return ComplexNum(r, i)
        else:
            raise ValueError("Комплексные числа могу складывать только между собой")


# Сложение
a = ComplexNum(1,3)
b = ComplexNum(4,-5)

print("a = " + str(a))
print("b = " + str(b))
print("a+b = " + str(a+b))

# Умножение
a = ComplexNum(1,-1)
b = ComplexNum(3,6)

print("a = " + str(a))
print("b = " + str(b))
print("a*b = " + str(a*b))
