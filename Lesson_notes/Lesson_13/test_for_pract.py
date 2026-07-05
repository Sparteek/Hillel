import unittest

from pract import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_concatenate_with_comma(self):
        result = concatenate_strings(["a", "b", "c"], ", ")
        self.assertEqual(result, "a, b, c")

    def test_concatenate_with_dash(self):
        result = concatenate_strings(["a", "b", "c"], " - ")
        self.assertEqual(result, "a - b - c")

    def test_concatenate_without_separator(self):
        result = concatenate_strings(["a", "b", "c"], "")
        self.assertEqual(result, "abc")

    def test_concatenate_one_string(self):
        result = concatenate_strings(["hello"], ", ")
        self.assertEqual(result, "hello")

    def test_concatenate_empty_list(self):
        result = concatenate_strings([], ", ")
        self.assertEqual(result, "")