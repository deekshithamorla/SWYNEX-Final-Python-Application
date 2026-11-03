import unittest
from main import calculate_total


class TestPythonApplication(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_total([2, 3]), 5)

    def test_multiple_numbers(self):
        self.assertEqual(calculate_total([1, 2, 3]), 6)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_total([])


if __name__ == "__main__":
    unittest.main()