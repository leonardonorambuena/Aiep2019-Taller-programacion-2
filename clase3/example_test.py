import unittest
from number_helper import NumberHelper

class ExampleTest(unittest.TestCase):

    #def test_uppercase_method(self):
        #name = 'LEONARDO'
        #upper_name = name.lower()
        #self.assertEqual(upper_name, 'LEONARDO')
    def test_is_par_method(self):
        self.assertTrue(NumberHelper.is_par(2))
        self.assertFalse(NumberHelper.is_par(1))

    def test_is_prime_method(self):
        self.assertTrue(NumberHelper.is_prime(5))
        self.assertFalse(NumberHelper.is_prime(6))


if __name__ == '__main__':
    unittest.main()

