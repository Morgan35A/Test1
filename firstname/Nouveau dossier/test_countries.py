import unittest
import sys
import os
import pycountry

from countries import pays

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCountries(unittest.TestCase):
    def testpositif(self):
        nom_pays = pycountry.countries.get(name = "Honduras")
        self.assertEqual(nom_pays.name, "Honduras")



if __name__ == '__main__':
    unittest.main()