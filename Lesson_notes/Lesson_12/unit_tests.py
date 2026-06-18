import unittest


class MyTestCase(unittest.TestCase):
    def test_our_first_test(self):
        actual_result = "Oleksii"
        expected_result = "Oleksii"

        assert actual_result == expected_result

    def test_second_one(self):
        actual_result = "Ol1eksii"
        expected_result = "Oleksii"



        self.assertEqual(actual_result, expected_result, 'is not aquals')