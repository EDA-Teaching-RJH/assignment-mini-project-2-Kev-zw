import unittest
from custom_library.math_utils import add_numbers, multiply_numbers

class TestMathUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 10), 15)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(5, 10), 50)

if __name__ == "__main__":
    unittest.main()
