import unittest

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """ Check that 1 is not prime"""
        self.assertFalse(is_prime(1))


    def test_2(self):
        """ Check that 2 is prime"""
        self.assertTrue(is_prime(2))

    def test_11(self):

        """ Check that 11 is  prime"""
        self.assertTrue(is_prime(11))

    
if __name__ == "__main__":
    unittest.main()