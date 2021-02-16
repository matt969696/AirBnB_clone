"""
Contains tests for Base class
"""

import unittest
import inspect
import pep8
import json
import console
import sys
from io import StringIO
from unittest.mock import patch
HBNBCommand = console.HBNBCommand


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of COnsole module"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base Class docstring"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)


class TestHBNBCommand_global(unittest.TestCase):
    """Unittests for testing HBNB console"""

    def test_prompt_string(self):
        """Tests the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Tests empty line"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help_quit(self):
        """Tests help quit"""
        h = "Stops the console and quit"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_show1(self):
        """Tests show function"""
        h = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_show2(self):
        """Tests show function"""
        h = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Matt"))
            self.assertEqual(h, output.getvalue().strip())

    def test_show3(self):
        """Tests show function"""
        h = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(h, output.getvalue().strip())
