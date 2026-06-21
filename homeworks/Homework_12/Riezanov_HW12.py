# Оберіть від 3 до 5 різних домашніх завдань
# перетворюєте їх у функції (якщо це потрібно)
# створіть в папці файл homeworks.py куди вставте ваші функції з дз
# та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
# імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
# На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.

import unittest
# from homeworks.Homework_9.Riezanov_HW9 import Romb
# from homeworks.Homework_8.Riezanov_HW8 import Student
# from homeworks.Homework_7.Riezanov_HW7 import longest_word, sum_even_numbers, average_function
from homeworks  import  Romb, Student, longest_word, sum_even_numbers, average_function


class TestRomb(unittest.TestCase):
    def setUp(self):
        self.romb = Romb(10,90)

    def test_side_a_saved_correctly(self):
        self.assertEqual(self.romb.side_a, 10)

    def test_angle_a_saved_correctly(self):
        self.assertEqual(self.romb.angle_a, 90)

    def test_angle_b_calculated_correctly(self):
        self.assertEqual(self.romb.angle_b, 90)

    def test_angle_b_calculated_for_max_angle_a(self):
        r = Romb(10,179)
        self.assertEqual(r.angle_b, 1)

    def test_angle_b_calculated_for_min_angle_a(self):
        r = Romb(10,1)
        self.assertEqual(r.angle_b, 179)

    def test_side_a_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            Romb(0,90)

    def test_angle_a_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            Romb(10,0)

    def test_angle_a_180_raises_value_error(self):
        with self.assertRaises(ValueError):
            Romb(10,180)

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student_1 = Student("John", "Doe", 44)

    def test_show_info_with_default_value(self):
        self.assertEqual(self.student_1.show_info(),
        "Name:John, Last_name:Doe, Age:44, Average_grade:76")

    def test_update_average_grade_changes(self):
        self.student_1.update_average_grade(50)
        self.assertEqual(self.student_1.get_average_grade(), 50)

    def test_show_info_after_grade_update(self):
        self.student_1.update_average_grade(50)
        self.assertEqual(self.student_1.show_info(),
        "Name:John, Last_name:Doe, Age:44, Average_grade:50")

class TestHomeworkFunctions(unittest.TestCase):
#Positive tests

    def test_longest_word_return_longest_word(self):
        self.assertEqual(longest_word(['cat','elephant','dog']), 'elephant')

    def test_average_function_returns_average_value(self):
        self.assertEqual(average_function([10,20,30]),20)

    def test_sum_even_numbers_returns_sum_of_even_numbers(self):
        self.assertEqual(sum_even_numbers([30, 40, 3, 5]), 70)

#Negative tests
    def test_longest_word_empty_list_raises_index_error(self):
        with self.assertRaises(IndexError):
            longest_word([])

    def test_average_function_with_string_raises_type_error(self):
        with self.assertRaises(TypeError):
             average_function([10,"hello",20])

    def test_sum_even_numbers_with_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            sum_even_numbers([2,"hello",4])



if __name__ == "__main__":
    unittest.main(verbosity=2)





