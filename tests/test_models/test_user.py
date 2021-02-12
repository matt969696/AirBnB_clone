#!/usr/bin/python3
"""
Contains tests for User class
"""

import unittest
import inspect
import pep8
import json
from datetime import datetime
from models import base_model
from models import user
BaseModel = base_model.BaseModel
User = user.User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.user_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestUser(unittest.TestCase):
    """Tests to check functionality of User class"""

    def test_class_type(self):
        """Tests if created class is User"""
        m1 = User()
        self.assertAlmostEqual(type(m1), User)

    def test_subclass_type(self):
        """Tests if created class is subclass of BaseModel"""
        m1 = User()
        self.assertIsInstance(m1, BaseModel)
        self.assertTrue(hasattr(m1, "id"))
        self.assertTrue(hasattr(m1, "created_at"))
        self.assertTrue(hasattr(m1, "updated_at"))

    def test_attribute_email(self):
        """Tests if User has an empty string email attribute"""
        m1 = User()
        self.assertTrue(hasattr(m1, "email"))
        self.assertEqual(m1.email, "")

    def test_attribute_password(self):
        """Tests if User has an empty string password attribute"""
        m1 = User()
        self.assertTrue(hasattr(m1, "password"))
        self.assertEqual(m1.password, "")

    def test_attribute_first_name(self):
        """Tests if User has an empty string first_name attribute"""
        m1 = User()
        self.assertTrue(hasattr(m1, "first_name"))
        self.assertEqual(m1.first_name, "")

    def test_attribute_last_name(self):
        """Tests if User has an empty string last_name attribute"""
        m1 = User()
        self.assertTrue(hasattr(m1, "last_name"))
        self.assertEqual(m1.last_name, "")

    def test_to_dict(self):
        """Tests to dict method"""
        m1 = User()
        dic1 = m1.to_dict()
        self.assertEqual(dic1["created_at"], m1.created_at.isoformat())
        self.assertEqual(dic1["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(dic1["__class__"], "User")

    def test_str(self):
        """Tests the __str__ method"""
        m1 = User()
        string = "[User] ({}) {}".format(m1.id, m1.__dict__)
        self.assertEqual(string, str(m1))
