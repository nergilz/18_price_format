import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):

    def test1_string_of_float(self):
        self.assertEqual(format_price('1234567.898'), '1 234 567.9')

    def test2_integer(self):
        self.assertEqual(format_price(1234567), '1 234 567')

    def test3_float(self):
        self.assertEqual(format_price(12345675.89), '12 345 675.89')

    def test4_rounding_of_a_number(self):
        self.assertEqual(format_price(12345675.8934545567), '12 345 675.89')

    def test5_bin_string_of_float(self):
        self.assertEqual(format_price(b'1234567.89'), '1 234 567.89')

    def test6_float_with_letter_in_string(self):
        self.assertIsNone(format_price('1234ghj.rt567'))

    def test7_string_of_number_with_duble_dot(self):
        self.assertIsNone(format_price('1234.567.89'))

    def test8_bin_string_of_number_with_double_dot(self):
        self.assertIsNone(format_price(b'1234ghj.rht567'))

    def test9_isinstance(self):
        self.assertIsInstance(format_price(1234567), str)

    def test10_price_is_list_of_number(self):
        self.assertIsNone(format_price([3, 5, 7]))

    def test11_price_is_dict(self):
        self.assertIsNone(format_price({'price': 345.67}))

    def test12_price_is_set_of_string(self):
        self.assertIsNone(format_price(('67.45', '234.56')))

    def test13_price_is_str_of_number_with_many_zero(self):
        self.assertEqual(format_price('7895.000000000'), '7 895')

    def test14_price_is_number_with_many_zero(self):
        self.assertEqual(format_price(7895.0000000000000), '7 895')

    def test15_result_not_none(self):
        self.assertIsNotNone(format_price('34567'))

    def test16_price_is_boolean_true(self):
        self.assertIsNone(format_price(True))

    def test17_price_is_boolean_false(self):
        self.assertIsNone(format_price(False))

    def test18_price_object_is_none(self):
        self.assertIsNone(format_price(None))


if __name__ == '__main__':

    unittest.main()
