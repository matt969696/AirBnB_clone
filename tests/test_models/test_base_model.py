#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pep8
import json
from datetime import datetime
from models import base_model
from unittest.mock import patch
BaseModel = base_model.BaseModel


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """Tests to check functionality of Base class"""

    def test_class_type(self):
        """Tests if created class is base model """
        m1 = BaseModel()
        self.assertAlmostEqual(type(m1), BaseModel)

    def test_attr(self):
        """Tests attributes creation"""
        m1 = BaseModel()
        m1.name = "Matt"
        self.assertEqual(m1.name, "Matt")
        m1.number = 123
        self.assertEqual(m1.number, 123)
        self.assertEqual(type(m1.id), str)
        self.assertEqual(type(m1.created_at), datetime)
        self.assertEqual(type(m1.updated_at), datetime)

    def test_to_dict(self):
        """Tests to dict method"""
        m1 = BaseModel()
        dic1 = m1.to_dict()
        self.assertEqual(dic1["created_at"], m1.created_at.isoformat())
        self.assertEqual(dic1["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(dic1["__class__"], "BaseModel")

    def test_datetime(self):
        """Tests that the time stamps are correct"""
        timefrom = datetime.now()
        m1 = BaseModel()
        timeto = datetime.now()
        self.assertEqual(m1.created_at, m1.updated_at)
        self.assertTrue(timefrom <= m1.created_at <= timeto)
        m2 = BaseModel()
        self.assertNotEqual(m1.created_at, m2.created_at)

    def test_str(self):
        """Tests the __str__ method"""
        m1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(m1.id, m1.__dict__)
        self.assertEqual(string, str(m1))

    @patch('models.storage')
    def test_save(self, mock):
        """Tests the save method"""
        m1 = BaseModel()
        old_created_at = m1.created_at
        old_updated_at = m1.updated_at
        m1.save()
        new_created_at = m1.created_at
        new_updated_at = m1.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
