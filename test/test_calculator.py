import unittest

from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        print 'Setup method'


    def tearDown(self):
        print 'Teardown method'


    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3,1), 4)


    def test_mult(self):
        c = Calculator()
        self.assertEqual(c.mult(3,1), 3)


    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div(3,1), 3)


    def test_div_with_zero(self):
        c = Calculator()
        self.assertRaises(ValueError, c.div, 3,0)


if __name__ == '__main__':
      unittest.main()
