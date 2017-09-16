import unittest
import ipaddress
from BitDoodle import bitdoodle
class TestStringMethods(unittest.TestCase):

    def test_joins(self):
        format_ = [40, 6, 4, 5, 5, 4, 64]
        values = [0x2607f6f099, 0xb, 0x7, 0xa, 0x9, 15, 0x123]
        dood = bitdoodle(format_)
        self.assertEqual(ipaddress.IPv6Address(u'2607:f6f0:992d:d49f::123'), dood.join(values))

        format_ = [8, 4, 6, 4, 6, 2, 2]
        values = [10, 10, 10, 4, 30, 2, 1]
        dood = bitdoodle(format_)
        self.assertEqual(ipaddress.IPv4Address(u'10.162.145.233'), dood.join(values))

        format_ = [8, 8, 4, 4]
        values = [255, 100, 10, 5]
        dood = bitdoodle(format_)
        self.assertEqual(16737445, dood.join(values))

        format_ = [40, 6, 4, 5, 5, 4, 64, 40, 24]
        values = [0x2607f6f099, 20, 10, 4, 30, 10, 35, 0x74317654, 16000000]
        dood = bitdoodle(format_)
        self.assertEqual(932520146808411025667857402430819217206404077264861144064, dood.join(values))

        format_ = [8, 8, 8, 8]
        values = [200, 200, 500, 200]  #500 too big for 8 bits
        dood = bitdoodle(format_)
        with self.assertRaises(Exception):
            dood.join(values)

        format_ = [8, 8, 8, 8]
        values = [200, 200, 200, 200, 200]  #too many values
        dood = bitdoodle(format_)
        with self.assertRaises(Exception):
            dood.join(values)

    def test_disjoins(self):
        format_ = [8, 8, 8, 8]
        value = 0b00001010000101000001111000101000
        expected_list = [10, 20, 30, 40]
        self.assertEqual(expected_list, bitdoodle(format_).disjoin(value))

        format_ = [8, 8, 8, 8]
        value = 0xffeeddcc
        expected_list = [255, 238, 221, 204]
        self.assertEqual(expected_list, bitdoodle(format_).disjoin(value))

        format_ = [4, 4, 8, 8, 8]
        value = 0xffeeddcc
        expected_list = [15, 15, 238, 221, 204]
        self.assertEqual(expected_list, bitdoodle(format_).disjoin(value))

    def test_fullcircle(self):
        #given a format and values, join the values, then disjoin them, and the values should be the same as the original values
        format_ = [23, 15, 100, 42, 65]
        values = [100, 200, 300, 400, 500]
        dood = bitdoodle(format_)
        self.assertEqual(values, dood.disjoin(dood.join(values)))

        #given a format and value, disjoin the value, then join the pieces, and the value should be the same as the original value
        format_ = [23, 15, 100, 42, 65]
        value = 100200300400500600700800
        dood = bitdoodle(format_)
        self.assertEqual(value, dood.join(dood.disjoin(value)))

if __name__ == '__main__':
    unittest.main()
