#!/usr/bin/python3
"""
Contains tests for Review class
"""

import unittest
import inspect
import pep8
import json
from datetime import datetime
from models import base_model
from models import review
BaseModel = base_model.BaseModel
Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.review_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestReview(unittest.TestCase):
    """Tests to check functionality of Review class"""

    def test_class_type(self):
        """Tests if created class is Review"""
        m1 = Review()
        self.assertAlmostEqual(type(m1), Review)

    def test_subclass_type(self):
        """Tests if created class is subclass of BaseModel"""
        m1 = Review()
        self.assertIsInstance(m1, BaseModel)
        self.assertTrue(hasattr(m1, "id"))
        self.assertTrue(hasattr(m1, "created_at"))
        self.assertTrue(hasattr(m1, "updated_at"))

    def test_attribute_place_id(self):
        """Tests if Review has an empty string place_id attribute"""
        m1 = Review()
        self.assertTrue(hasattr(m1, "place_id"))
        self.assertEqual(m1.place_id, "")

    def test_attribute_user_id(self):
        """Tests if Review has an empty string user_id attribute"""
        m1 = Review()
        self.assertTrue(hasattr(m1, "user_id"))
        self.assertEqual(m1.user_id, "")

    def test_attribute_text(self):
        """Tests if Review has an empty string text attribute"""
        m1 = Review()
        self.assertTrue(hasattr(m1, "text"))
        self.assertEqual(m1.text, "")

    def test_to_dict(self):
        """Tests to dict method"""
        m1 = Review()
        dic1 = m1.to_dict()
        self.assertEqual(dic1["created_at"], m1.created_at.isoformat())
        self.assertEqual(dic1["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(dic1["__class__"], "Review")

    def test_str(self):
        """Tests the __str__ method"""
        m1 = Review()
        string = "[Review] ({}) {}".format(m1.id, m1.__dict__)
        self.assertEqual(string, str(m1))
