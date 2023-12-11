#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def test_base_crt(self):
        pv = Base()
        self.assertIsInstance(pv, Base)
        self.assertIsNotNone(pv.id)

    def test_chk(self):
        pv = Base(135)
        self.assertEqual(pv.id, 135)

    def test_nb_ob(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_ob_2(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_obj_instant(self):
        pv = Base()
        self.assertEqual(str(type(pv)), "<class 'models.base.Base'>")

    def tes_obj_dict(self):
        pv = Base()
        self.assertEqual(str(type(pv.__dict__)), "<class 'dict'>")
        self.assertEqual(pv.__dict__, "{'id': 1}")


if __name__ == '__main__':
    unittest.main()
