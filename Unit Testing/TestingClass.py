# Class Testing

import unittest
from ClassScript import printer, printerError

class test_printerclass(unittest.TestCase):
    
    def setUp(self):
        self.printer_ = printer(pages_per_sec=2.0, capacity=300)
        
        
    def test_within_capacity(self): 
        self.printer_.print_(25)
        # message = self.printer_.print_(25)
        # self.assertEqual(f'Printed 25 pages in 12.50 seconds', message)
        
        
    def test_within_outside_capacity(self):
        with self.assertRaises(printerError):
            self.printer_.print_(350)
            
            
    def test_within_excat_capacity(self):
        self.printer_.print_(300)
        
        
    def test_printer_speed(self):
        pages = 10
        expected = 'Printed 10 pages in 5.00 seconds'
        result = self.printer_.print_(pages)
        
        self.assertEqual(result, expected)
        
        
    def test_printer_two_decimal_places(self):
        fast_printer = printer(pages_per_sec=3.0, capacity=300)
        pages = 11
        expected = 'Printed 11 pages in 3.67 seconds'
        result = fast_printer.print_(pages)
        
        self.assertEqual(result, expected)
        
        
    def test_multiple_print_runs(self): 
        self.printer_.print_(25)
        self.printer_.print_(50)
        self.printer_.print_(225)
        
        
    def test_multiple_print_runs_with_errors(self): 
        self.printer_.print_(25)
        self.printer_.print_(50)
        self.printer_.print_(225)
        
        with self.assertRaises(printerError):
            self.printer_.print_(1)

    
if __name__ == '__main__':
    unittest.main()
