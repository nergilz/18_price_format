import unittest
import format_price


class FormatPriceTest(unittest.TestCase):


    def test1_main(self):
        self.assertEqual(format_price.main('1234567.89'), '1 234 567.89')

    def test2_main_int(self):
        self.assertEqual(format_price.main(1234567), '1 234 567.0')

    def test3_main(self):
        self.assertEqual(format_price.main(12345675.89), '12 345 675.89')

    def test4_main(self):
        self.assertEqual(format_price.main('1234ghj.rt567'), None)

    def test5_main(self):
        self.assertEqual(format_price.main('1234.567.89'), None)

    def test6_main(self):
        self.assertEqual(format_price.main(b'1234567.89'), '1 234 567.89')

    def test7_main(self):
        self.assertEqual(format_price.main(b'1234ghj.rht567'), None)


if __name__ == '__main__':

    unittest.main()