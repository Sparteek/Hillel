import unittest

from Lesson_notes.Lesson_12.new_file import get_passangers

def sum_values(a, b):
    return a + b


class TestTest(unittest.TestCase):
    def test_fun(self):
        result = sum_values(1, 2)
        self.assertEqual(result, 3)


# try,exapt,asert
# одна функція один тест, (бажано)
