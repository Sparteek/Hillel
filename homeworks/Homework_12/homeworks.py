class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError('side_a must be greater than 0')

        if key == 'angle_a':
            if value <= 0 or value >= 180:
                 raise ValueError('angle_a must be between 0 and 180')

            super().__setattr__("angle_b", 180 - value)

        super().__setattr__(key, value)


class Student:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.__average_grade = 76

    def get_average_grade(self):
        return self.__average_grade

    def update_average_grade(self, grade):
        self.__average_grade = grade #я тут використав сама '=' бо в завданні сказано "метод який дозволяє змінювати"

    def show_info(self):
        return f'Name:{self.name}, Last_name:{self.last_name}, Age:{self.age}, Average_grade:{self.get_average_grade()}'

student_1 = Student("John", "Doe", 44)

words = ['Hello', 'World', 'Tartartfsffsafafs', 'Gradddppedd']

def longest_word(words):
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
print(longest_word(words))

def sum_even_numbers(numbers):
    """Returns the sum of even numbers from a list."""
    even_number_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_number_sum += number
    return even_number_sum

numbers = [10,1,4,5,6,7]

def average_function(numbers):
    if numbers == []:
        return f'The list is empty {numbers}'

    average = sum(numbers) / len(numbers)
    return average
print(average_function(numbers))