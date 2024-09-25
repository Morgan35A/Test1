import unittest
import sys 
import os
from io import StringIO
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



from firstname import greet_user
class FirstName(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_name_argument(self, mock_stdout):
        greet_user(name="diego")
        self.assertEqual(mock_stdout.getvalue().strip(), 'merci diego')

        






    def test_positif(self):
        self.assertIsNotNone

    def test_negatif(self):
        self.assertIsNotNone
    if test_positif == True: 
        print(test_positif)
    else:
        print(test_negatif)
if __name__ == '__main__':
    unittest.main()

