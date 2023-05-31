"""Tests all function in src.pftesting_richelbilderbeek.easy_questions."""
import unittest

from src.pftesting_richelbilderbeek.tdd_questions import (
    is_zero,
)


class TestEasySolutions(unittest.TestCase):

    """Class to test the functions in src.pftesting_richelbilderbeek.easy_questions."""

    def test_is_zero(self):
        """Test 'is_zero'."""
        self.assertIsNotNone(is_zero.__doc__)
        self.assertTrue(is_zero(0))
        self.assertTrue(is_zero(0.0))
        self.assertFalse(is_zero(1))
        self.assertRaises(TypeError, is_zero, {1, 2})
        self.assertRaises(TypeError, is_zero, "I am a string")

    def test_is_prime(self):
        self.assertTrue(is_prime(1))
        self.assertFalse(is_prime(4))
