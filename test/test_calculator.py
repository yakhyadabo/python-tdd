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

    def test_sum(self):
        c = Calculator()
        self.assertEqual(c.sum(3,1,3,4,0), 11)


    def test_mult(self):
        c = Calculator()
        self.assertEqual(c.mult(3,1), 3)


    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div(3,1), 3)


    def test_div_with_zero(self):
        c = Calculator()
        self.assertRaises(ValueError, c.div, 3,0)


    def test_fact_zero(self):
        c = Calculator()
        self.assertEqual(c.fact(0),1)
        

    def test_fact_4(self):
        c = Calculator()
        self.assertEqual(c.fact(4),24)
        

if __name__ == '__main__':
      unittest.main()
