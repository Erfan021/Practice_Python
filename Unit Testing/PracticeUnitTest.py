# Unit Test Practice Exercise

import unittest
import PracticeScript

class testScript(unittest.TestCase):
    def test_input(self):
        res = PracticeScript.run_guess(5, 5)
        self.assertTrue(res)
        
    
    def test_input_wrong_guess(self):
        res = PracticeScript.run_guess(5, 0)
        self.assertFalse(res)
        
        
    def test_input_wrong_number(self):
        res = PracticeScript.run_guess(5, 11)
        self.assertFalse(res)
        
        
    def test_input_wrong_type(self):
        res = PracticeScript.run_guess(5, '1')
        self.assertFalse(res)
    
    
if __name__ == '__main__':
    unittest.main()
