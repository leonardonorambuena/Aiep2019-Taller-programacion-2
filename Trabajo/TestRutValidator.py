import unittest
from RutValidator import RutValidator

class TestRutValidator(unittest.TestCase):

    def test_invalid_rut(self):
        rut_validator = RutValidator('1515155-5')
        self.assertFalse(rut_validator.is_valid())

    def test_rut_validator_without_dv(self):
        rut_validator = RutValidator('16.836.431-8')
        self.assertTrue(rut_validator.is_valid())
        self.assertEqual('8', rut_validator.dv)
        self.assertEqual(16836431, rut_validator.numbers)
        self.assertEqual('16.836.431', rut_validator.formated_numbers)

    def test_rut_validator_with_dv(self):
        rut_validator = RutValidator('17138270', 'k')
        self.assertTrue(rut_validator.is_valid())
        self.assertEqual('K', rut_validator.dv)
        self.assertEqual(17138270, rut_validator.numbers)
        self.assertEqual('17.138.270', rut_validator.formated_numbers)

        second_rut = RutValidator('17.138.270', 'K')
        self.assertTrue(second_rut.is_valid())
        self.assertEqual('K', second_rut.dv)
        self.assertEqual(17138270, second_rut.numbers)
        self.assertEqual('17.138.270', second_rut.formated_numbers)


if __name__ == '__main__':
    unittest.main()