import unittest
import sys 
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from test_unitaire import addition 

class TestAddition(unittest.TestCase):
    def test_positif(self):
        self.assertEqual(addition(2, 3), 5)

    def test_negatif(self):
        self.assertEqual(addition(-1, 1), 0)
        
if __name__ == '__main__':
    unittest.main()