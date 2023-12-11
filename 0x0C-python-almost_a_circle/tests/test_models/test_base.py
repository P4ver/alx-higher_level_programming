#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_crt(self):
        pv = Base()
        self.assertIsInstance(pv, Base)
        self.assertIsNotNone(pv.id)

    def test_chk(self):
        pv = Base(135)
        self.assertEqual(pv.id, 135)


if __name__ == '__main__':
    unittest.main()
