#!/usr/bin/env python3
import unittest
from sol import numOfYears

class test_assignment(unittest.TestCase):
    def test_1(self):
        self.assertEqual(numOfYears(4,7), 2)
        
    def test_2(self):
        self.assertEqual(numOfYears(4,9), 3)
    
    def test_3(self):
        self.assertEqual(numOfYears(1,1), 1)
    
    def test_4(self):
        self.assertEqual(numOfYears(5,8), 2)
   
    
if __name__ == "__main__":
    unittest.main()


