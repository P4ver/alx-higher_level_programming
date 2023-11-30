#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_nmb(self):
        res_tl = max_integer([98, 96, 23, 54])
        self.assertEqual(res_tl, 98)
    def test_max_nmb(self):
        res_tl = max_integer([9, 7, 23, 5])
        self.assertEqual(res_tl, 23)
    def test_one_int(self):
        res_tl = max_integer([498])
        self.assertEqual(res_tl, 498)


if __name__ == "__main__":
    unittest.main()
