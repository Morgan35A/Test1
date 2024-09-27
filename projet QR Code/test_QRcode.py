import unittest
import sys
import os
from unittest import TestCase

import qrcode

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from jinja2.compiler import generate
from six import assertCountEqual
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from QRCode import QRCodeGeneratorApp




class QRCodeGenerator(unittest.TestCase):
    def is_valid_url(self, url):
        url_regex = re.compile(r'https?://(?:www\.)?[a-zA-Z0-9./]+')
        return bool(url_regex.match(url))
    def test_valid_url(self):
        test_url = "https://www.youtube.com"
        test_url2 = "yrhur"
        result = self.is_valid_url(test_url)
        result2 = self.is_valid_url(test_url2)
        print(f"Est-ce-que '{test_url}' est une URL valide? {result}")
        print(f"Est-ce-que '{test_url2}' est une URL valide? {result2}")
        self.assertTrue(result)
        self.assertFalse(result2)



if __name__ == '__main__':
    unittest.main()