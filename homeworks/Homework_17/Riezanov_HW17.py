#Task №1
print("Генератори Task №1: Напишіть генератор, який повертає послідовність парних чисел від 0 до N. ")
def even_numbesr(num):
    current = 0

    while current < num:
            yield current
            current += 2

for num in even_numbesr(11):
    print(num)

print("-" *  100)
print("Генератори Task №2: Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.")


#Task №2
def fibonacci(num):
    first = 0
    second = 1

    while first < num:
        yield first
        first, second = second, first + second


for num in fibonacci(100):
    print(num)

print("-" *  100)
print("Ітератори Task №1: Реалізуйте ітератор для зворотного виведення елементів списку. ")

class ReversIterator:
    def __init__(self, num):
        self.num = num
        self.index = len(self.num) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.num[self.index]
        self.index -= 1
        return value

numbers = [3,5,10, 20, 30, 40]

reverse_numbers = ReversIterator(numbers)

for num in reverse_numbers:
    print(num)

print("-" *  100)
print("Ітератори Task №2: Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N. ")

class PairIterator:
    def __init__(self, num):
        self.num = num
        self.current = 0  #можно почати з 2 але як Я почитав 0 в Python вважається парним числом.

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.num:
            raise StopIteration

        value = self.current
        self.current += 2
        return value

for num in PairIterator(10):
    print(num)
#можно і в ручну
pair_it = PairIterator(10)
print(next(pair_it))
print(next(pair_it))
print(next(pair_it))

print("-" *  100)
print("Декоратори Task №1: Напишіть декоратор, який логує аргументи та результати викликаної функції.")

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функція: {func.__name__}")
        print("Аргументи:", args, kwargs)

        result =  func(*args, **kwargs)

        print("Результат:", result)
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def subtract(a, b):
    return a - b

@log_decorator
def multiply(a, b):
    return a * b


add(1, 2)
subtract(5, 2)
multiply(10, 2)

print("-" *  100)
print("Декоратори Task №2: Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.")

def execution_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            print("Error:", error)

    return wrapper


@execution_decorator
def get_item(item, index):
    return item[index]

print(get_item([1, 0], 0))
print(get_item([10,20,30], 3))
print(get_item([10,20,30,40,50,60,70], 10))

@execution_decorator
def divide_execpt(a, b):
    return a / b
print(divide_execpt(1, 2))
print(divide_execpt(1, 0))

@execution_decorator
def convert_to_int(value):
    return int(value)

print(convert_to_int(111))
print(convert_to_int("Max"))