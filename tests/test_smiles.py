import unittest

from smiles import smiles


class TestMethods(unittest.TestCase):
    def test_smile(self):
        self.assertEqual(smiles.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
