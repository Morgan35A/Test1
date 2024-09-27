import unittest
from unittest import TestCase
from unittest.mock import patch
from PIL import ImageTk
from QRCode import QRCodeGeneratorApp  # Assurez-vous que ce chemin est correct
import tkinter as tk
import re


class TestQRCodeGeneratorApp(unittest.TestCase):

    def setUp(self):
        """Cette méthode est exécutée avant chaque test. Elle crée une instance de Tkinter et de votre application."""
        self.root = tk.Tk()
        self.app = QRCodeGeneratorApp(self.root)

    def tearDown(self):
        """Cette méthode est exécutée après chaque test. Elle détruit la fenêtre Tkinter."""
        self.root.destroy()

    @patch('QRCode.messagebox.showwarning')
    def test_QRCode_with_empty_url(self, mock_showwarning):
        """Teste la génération du QR code avec une URL vide."""
        self.app.entry.delete(0, tk.END)  # Simule l'entrée vide
        self.app.generate_qr_code()

        # Vérifie que l'avertissement a été affiché
        mock_showwarning.assert_called_once_with("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.")

    def test_QRCode_with_valid_url(self):
        """Teste la génération du QR code avec une URL valide."""
        valid_url = "https://www.youtube.com"
        self.app.entry.insert(0, valid_url)  # Simule l'insertion d'une URL valide dans l'entrée
        self.app.generate_qr_code()

        # Vérifie si le label de l'image contient bien une image
        self.assertIsInstance(self.app.qr_image, ImageTk.PhotoImage)
        self.assertTrue(self.app.image_label.cget('image'))  # Vérifie si l'image est attribuée au label


class TestQRCodeGenerator(unittest.TestCase):
    def is_valid_url(self, url):
        """Vérifie si l'URL est valide."""
        url_regex = re.compile(r'https?://(?:www\.)?[a-zA-Z0-9./]+')
        return bool(url_regex.match(url))

    def test_valid_url(self):
        """Test pour vérifier la validité des URLs."""
        test_url1 = "https://www.youtube.com"
        test_url2 = "invalid-url"
        result1 = self.is_valid_url(test_url1)
        result2 = self.is_valid_url(test_url2)

        self.assertTrue(result1)  # test_url1 doit être valide
        self.assertFalse(result2)  # test_url2 doit être invalide

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



if __name__ == "__main__":
    unittest.main()