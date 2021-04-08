import unittest

from calculator import calculator


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 2), -1)


if __name__ == '__main__':
    unittest.main()
