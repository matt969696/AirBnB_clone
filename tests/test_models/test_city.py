#!/usr/bin/python3
"""
Contains tests for City class
"""

import unittest
import inspect
import pep8
import json
from datetime import datetime
from models import base_model
from models import city
BaseModel = base_model.BaseModel
City = city.City


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(city.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.city_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    """Tests to check functionality of City class"""

    def test_class_type(self):
        """Tests if created class is City"""
        m1 = City()
        self.assertAlmostEqual(type(m1), City)

    def test_subclass_type(self):
        """Tests if created class is subclass of BaseModel"""
        m1 = City()
        self.assertIsInstance(m1, BaseModel)
        self.assertTrue(hasattr(m1, "id"))
        self.assertTrue(hasattr(m1, "created_at"))
        self.assertTrue(hasattr(m1, "updated_at"))

    def test_attribute_state_id(self):
        """Tests if City has an empty string state_id attribute"""
        m1 = City()
        self.assertTrue(hasattr(m1, "state_id"))
        self.assertEqual(m1.state_id, "")

    def test_attribute_name(self):
        """Tests if City has an empty string name attribute"""
        m1 = City()
        self.assertTrue(hasattr(m1, "name"))
        self.assertEqual(m1.name, "")

    def test_to_dict(self):
        """Tests to dict method"""
        m1 = City()
        dic1 = m1.to_dict()
        self.assertEqual(dic1["created_at"], m1.created_at.isoformat())
        self.assertEqual(dic1["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(dic1["__class__"], "City")

    def test_str(self):
        """Tests the __str__ method"""
        m1 = City()
        string = "[City] ({}) {}".format(m1.id, m1.__dict__)
        self.assertEqual(string, str(m1))
