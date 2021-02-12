#!/usr/bin/python3
"""
Contains tests for State class
"""

import unittest
import inspect
import pep8
import json
from datetime import datetime
from models import base_model
from models import state
BaseModel = base_model.BaseModel
State = state.State


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.state_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):
    """Tests to check functionality of State class"""

    def test_class_type(self):
        """Tests if created class is State"""
        m1 = State()
        self.assertAlmostEqual(type(m1), State)

    def test_subclass_type(self):
        """Tests if created class is subclass of BaseModel"""
        m1 = State()
        self.assertIsInstance(m1, BaseModel)
        self.assertTrue(hasattr(m1, "id"))
        self.assertTrue(hasattr(m1, "created_at"))
        self.assertTrue(hasattr(m1, "updated_at"))

    def test_attribute_name(self):
        """Tests if State has an empty string name attribute"""
        m1 = State()
        self.assertTrue(hasattr(m1, "name"))
        self.assertEqual(m1.name, "")

    def test_to_dict(self):
        """Tests to dict method"""
        m1 = State()
        dic1 = m1.to_dict()
        self.assertEqual(dic1["created_at"], m1.created_at.isoformat())
        self.assertEqual(dic1["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(dic1["__class__"], "State")

    def test_str(self):
        """Tests the __str__ method"""
        m1 = State()
        string = "[State] ({}) {}".format(m1.id, m1.__dict__)
        self.assertEqual(string, str(m1))
