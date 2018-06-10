import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):

    def test1_string_of_float(self):
        self.assertEqual(format_price('1234567.89'), '1 234 567.89')

    def test2_integer(self):
        self.assertEqual(format_price(1234567), '1 234 567.0')

    def test3_float(self):
        self.assertEqual(format_price(12345675.89), '12 345 675.89')

    def test4_bin_string_of_float(self):
        self.assertEqual(format_price(b'1234567.89'), '1 234 567.89')

    def test5_float_with_letter_in_string(self):
        self.assertIsNone(format_price('1234ghj.rt567'))

    def test6_string_of_munber_with_duble_dot(self):
        self.assertIsNone(format_price('1234.567.89'))

    def test7_bin_string_of_number_with_duble_dot(self):
        self.assertIsNone(format_price(b'1234ghj.rht567'))

    def test8_isinstance(self):
        self.assertIsInstance(format_price(1234567), str)


if __name__ == '__main__':

    unittest.main()