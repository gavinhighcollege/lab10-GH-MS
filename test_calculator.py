import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(2,3), 5)
        self.assertEqual(calculator.add(-1,1),0)
        self.assertEqual(calculator.add(0,0),0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(calculator.sub(5, 3), 2)
        self.assertEqual(calculator.sub(0, 5), -5)
        self.assertEqual(calculator.sub(-2, -2), 0)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.log(10, 100), 2.0)
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)
        self.assertAlmostEqual(calculator.log(4, 16), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(1, 10)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
        def test_multiply(self):
            self.assertEqual(calculator.multiply(3, 4), 12)
            self.assertEqual(calculator.multiply(-2, 5), -10)

        def test_divide(self):
            self.assertAlmostEqual(calculator.divide(10, 2), 5)
            with self.assertRaises(ZeroDivisionError):
                calculator.divide(10, 0)

        def test_log_invalid_argument(self):
            with self.assertRaises(ValueError):
                calculator.logarithm(-2, 10)
            with self.assertRaises(ValueError):
                calculator.logarithm(10, -2)

        def test_hypotenuse(self):
            self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
            self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

        def test_sqrt(self):
            self.assertAlmostEqual(calculator.square_root(9), 3)
            with self.assertRaises(ValueError):
                calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()