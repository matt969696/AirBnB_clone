#!/usr/bin/python3
"""
Contains tests for Place class
"""

import unittest
import inspect
import pep8
import json
from datetime import datetime
from models import base_model
from models import place
BaseModel = base_model.BaseModel
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_funcs = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.place_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestPlace(unittest.TestCase):
    """Tests to check functionality of Place class"""

    def test_class_type(self):
        """Tests if created class is Place"""
        m1 = Place()
        self.assertAlmostEqual(type(m1), Place)

    def test_subclass_type(self):
        """Tests if created class is subclass of BaseModel"""
        m1 = Place()
        self.assertIsInstance(m1, BaseModel)
        self.assertTrue(hasattr(m1, "id"))
        self.assertTrue(hasattr(m1, "created_at"))
        self.assertTrue(hasattr(m1, "updated_at"))

    def test_attribute_city_id(self):
        """Tests if Place has an empty string city_id attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "city_id"))
        self.assertEqual(m1.city_id, "")

    def test_attribute_user_id(self):
        """Tests if Place has an empty string user_id attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "user_id"))
        self.assertEqual(m1.user_id, "")

    def test_attribute_name(self):
        """Tests if Place has an empty string name attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "name"))
        self.assertEqual(m1.name, "")

    def test_attribute_description(self):
        """Tests if Place has an empty string description attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "description"))
        self.assertEqual(m1.description, "")

    def test_attribute_number_rooms(self):
        """Tests if Place has a 0 integer number_rooms attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "number_rooms"))
        self.assertEqual(type(m1.number_rooms), int)
        self.assertEqual(m1.number_rooms, 0)

    def test_attribute_number_bathrooms(self):
        """Tests if Place has a 0 integer number_bathrooms attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "number_bathrooms"))
        self.assertEqual(type(m1.number_bathrooms), int)
        self.assertEqual(m1.number_bathrooms, 0)

    def test_attribute_max_guest(self):
        """Tests if Place has a 0 integer max_guest attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "max_guest"))
        self.assertEqual(type(m1.max_guest), int)
        self.assertEqual(m1.max_guest, 0)

    def test_attribute_price_by_night(self):
        """Tests if Place has a 0 integer price_by_night attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "price_by_night"))
        self.assertEqual(type(m1.price_by_night), int)
        self.assertEqual(m1.price_by_night, 0)

    def test_attribute_latitude(self):
        """Tests if Place has a 0 integer latitude attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "latitude"))
        self.assertEqual(type(m1.latitude), float)
        self.assertEqual(m1.latitude, 0.0)

    def test_attribute_longitude(self):
        """Tests if Place has a 0 integer longitude attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "longitude"))
        self.assertEqual(type(m1.longitude), float)
        self.assertEqual(m1.longitude, 0.0)

    def test_attribute_amenity_ids(self):
        """Tests if Place has an empty list amenity_ids attribute"""
        m1 = Place()
        self.assertTrue(hasattr(m1, "amenity_ids"))
        self.assertEqual(type(m1.amenity_ids), list)
        self.assertEqual(len(m1.amenity_ids), 0)

    def test_to_dict(self):
        """Tests to dict method"""
        m1 = Place()
        dic1 = m1.to_dict()
        self.assertEqual(dic1["created_at"], m1.created_at.isoformat())
        self.assertEqual(dic1["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(dic1["__class__"], "Place")

    def test_str(self):
        """Tests the __str__ method"""
        m1 = Place()
        string = "[Place] ({}) {}".format(m1.id, m1.__dict__)
        self.assertEqual(string, str(m1))
