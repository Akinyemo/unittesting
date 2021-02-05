import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.addition(20,5),25)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(20,5),15)
    
    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(20,5),100)

    def test_divison(self):
        self.assertEqual(calculator.division(20,5),4)

if __name__ == "__main__":
    unittest.main()