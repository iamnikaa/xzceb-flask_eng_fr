"""Unittest module for testing translator module"""
import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TranslatorTest(unittest.TestCase):
    """Test functions for english to french and french to english translator functions"""

    def test_englishToFrench(self):
        """Tests english_to_french function"""
        self.assertNotEqual(englishToFrench("Hello"), "")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        """Tests french_to_english function"""
        self.assertNotEqual(frenchToEnglish("Hello"), "")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main(verbosity=2)
