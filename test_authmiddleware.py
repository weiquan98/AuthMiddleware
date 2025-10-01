# test_authmiddleware.py
"""
Tests for AuthMiddleware module.
"""

import unittest
from authmiddleware import AuthMiddleware

class TestAuthMiddleware(unittest.TestCase):
    """Test cases for AuthMiddleware class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AuthMiddleware()
        self.assertIsInstance(instance, AuthMiddleware)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AuthMiddleware()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
