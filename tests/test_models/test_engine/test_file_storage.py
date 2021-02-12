#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine import file_storage
from models import storage
FileStorage = file_storage.FileStorage


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of file_storage"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that models/file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/.../test_file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        path = 'tests/test_models/test_engine/test_file_storage.py'
        res = pep8style.check_files([path])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class and functions"""

    def test_attr(self):
        """Tests attributes creation"""
        s1 = FileStorage()
        self.assertTrue(hasattr(s1, "_FileStorage__objects"))
        self.assertTrue(hasattr(s1, "_FileStorage__file_path"))

    def test_attr_all(self):
        """Tests all function should return dict"""
        s1 = FileStorage()
        d1 = s1.all()
        self.assertEqual(type(d1), dict)
        self.assertIs(d1, s1._FileStorage__objects)

    def test_new(self):
        """Tests the new function"""
        s1 = FileStorage()
        s1._FileStorage__objects = {}
        d1 = {}
        m1 = BaseModel()
        s1.new(m1)
        m2 = User()
        s1.new(m2)
        d1["BaseModel." + m1.id] = m1
        d1["User." + m2.id] = m2
        t1 = s1.all()
        self.assertDictEqual(t1, d1)

    def test_save_reload(self):
        """Tests the save and reload functions"""
        if os.path.isfile('file.json'):
            os.rename("file.json", "file.jsonSAVE")
        m1 = BaseModel()
        m1.save()
        storage.reload()
        ld = storage.all()
        self.assertDictEqual(ld["BaseModel." + m1.id].to_dict(), m1.to_dict())
        os.remove("file.json")
        if os.path.isfile('file.jsonSAVE'):
            os.rename("file.jsonSAVE", "file.json")
