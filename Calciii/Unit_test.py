import unittest
from Calci_code import Calculator

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    '''@unittest.skip('Some reason')'''
    def test_mul(self):
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    def test_div(self):
        self.calc = Calculator()
        result = self.calc.div(10, 2)
        expected = 5
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
