# Unit test script

import unittest
import FunctionsScript

class test_Functions(unittest.TestCase):
    def test_divide_function(self):
        dividend = 15
        divisor = 3
        expected_res = 5.0
        self.assertAlmostEqual(FunctionsScript.divide(dividend, divisor), expected_res,
                               delta= 0.0001)
        
        
    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_res = -5.0
        self.assertAlmostEqual(FunctionsScript.divide(dividend, divisor), expected_res,
                               delta= 0.0001)
        
        
    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_res = 0
        self.assertEqual(FunctionsScript.divide(dividend, divisor), expected_res) 
        
        
    def test_divide_divisor_zero(self):
        with self.assertRaises(ValueError):
            FunctionsScript.divide(25,0)
 
    
    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            FunctionsScript.multiply()
            
    
    def test_multiply_single_value(self):
        expected = 10
        self.assertEqual(FunctionsScript.multiply(expected), expected)
        
        
    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(FunctionsScript.multiply(expected), expected)   
        
        
    def test_multiply_result(self):
        inputs = (3,5)
        expected = 15
        self.assertEqual(FunctionsScript.multiply(*inputs), expected)
        
        
    def test_multiply_result_with_zero(self):
        inputs = (3,5,0)
        expected = 0
        self.assertEqual(FunctionsScript.multiply(*inputs), expected)
        
        
    def test_multiply_negative(self):
        inputs = (3,5,-2)
        expected = -30
        self.assertEqual(FunctionsScript.multiply(*inputs), expected)
        
        
    def test_multiply_floats(self):
        inputs = (3, 2.0)
        expected = 6.0
        self.assertEqual(FunctionsScript.multiply(*inputs), expected)
    
       
if __name__ == '__main__':
    unittest.main()