# Unit Test

import unittest
import testingScript

class mainTest(unittest.TestCase):
    def setUp(self):
        print('About test a function')
        

    def test_stuff_do(self):
        test_num = 10
        result = testingScript.stuff_do(test_num)
        self.assertEqual(result, 15)
        
    
    def test_stuff_do_2(self):
        test_num = 'work'
        result = testingScript.stuff_do(test_num)
        self.assertIsInstance(result, ValueError)
        
    
    def test_stuff_do_3(self):
        test_num = None
        result = testingScript.stuff_do(test_num)
        self.assertEqual(result, 'Enter number please')
        

    def test_stuff_do_4(self):
        test_num = ''
        result = testingScript.stuff_do(test_num)
        self.assertEqual(result, 'Enter number please')
        
        
    def tearDown(self):
        print('Cleaning up')
        

if __name__ == '__main__':
    unittest.main()

