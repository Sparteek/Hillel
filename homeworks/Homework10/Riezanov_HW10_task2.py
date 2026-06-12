# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def figure_area(self):
        pass

    @abstractmethod
    def figure_perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def figure_area(self):
        return (f'Площа квадрата = {self.__side * self.__side}')
    def figure_perimeter(self):
        return (f'Периметр квадрата = {self.__side * 4}')

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def figure_area(self):
        return (f'Площа прямокутника = {self.__side_a * self.__side_b}')

    def figure_perimeter(self):
        return (f'Периметр прямокутника = {2 * (self.__side_a + self.__side_b)}')

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    def figure_area(self):
        return (f'Площа круга = {math.pi * self.__radius ** 2:.2f}')
    def figure_perimeter(self):
        return (f'Периметр круга = {2 * math.pi * self.__radius:.2f}')

s = Square(5)
# print(s.figure_area())
# print(s.figure_perimeter())

r = Rectangle(2, 3)
# print(r.figure_area())
# print(r.figure_perimeter())

c = Circle(3)
# print(c.figure_area())
# print(c.figure_perimeter())

figure_list = [s, r, c]
for figure in figure_list:
    print(figure.figure_area())
    print(figure.figure_perimeter())