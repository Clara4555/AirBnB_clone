#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNBCommandPrompting(unittest.TestCase):
    """Unittests for HBNBCommand command prompting."""

    def test_prompt(self):
        """Test that the prompt is set correctly."""
        self.assertEqual(HBNBCommand().prompt, "(hbnb) ")


class TestHBNBCommandHelp(unittest.TestCase):
    """Unittests for HBNBCommand help command."""

    def test_help(self):
        """Test that the help command displays help message."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("help")
            output = mock_stdout.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)


class TestHBNBCommandExit(unittest.TestCase):
    """Unittests for HBNBCommand exit command."""

    def test_quit_command(self):
        """Test that the quit command exits the console."""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_EOF_command(self):
        """Test that the EOF command exits the console."""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")

    def test_exit(self):
        """Test that the exit command exits the console."""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("exit")


class TestHBNBCommandCreate(unittest.TestCase):
    """Unittests for HBNBCommand create command."""

    def setUp(self):
        """Set up the test environment."""
        self.storage_file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = self.storage_file_path

    def test_create_missing_class(self):
        """Test create command with missing class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with an invalid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create(self):
        """Test create command with a valid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"show User {output}")
            output_show = mock_stdout.getvalue()
            self.assertIn(output, output_show)


class TestHBNBCommandShow(unittest.TestCase):
    """Unittests for HBNBCommand show command."""

    def setUp(self):
        """Set up the test environment."""
        self.storage_file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = self.storage_file_path

    def test_show_missing_class(self):
        """Test show command with missing class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with an invalid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show User")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with an invalid instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show User 12345")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_show(self):
        """Test show command with a valid class and instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create User")
            obj_id = mock_stdout.getvalue().strip()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"show User {obj_id}")
            output = mock_stdout.getvalue()
            self.assertIn(obj_id, output)


class TestHBNBCommandAll(unittest.TestCase):
    """Unittests for HBNBCommand all command."""

    def setUp(self):
        """Set up the test environment."""
        self.storage_file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = self.storage_file_path

    def test_all_missing_class(self):
        """Test all command with missing class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("User", output)

    def test_all_invalid_class(self):
        """Test all command with an invalid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_all(self):
        """Test all command with a valid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create User")
            obj_id = mock_stdout.getvalue().strip()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all User")
            output = mock_stdout.getvalue()
            self.assertIn(obj_id, output)


class TestHBNBCommandDestroy(unittest.TestCase):
    """Unittests for HBNBCommand destroy command."""

    def setUp(self):
        """Set up the test environment."""
        self.storage_file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = self.storage_file_path

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with an invalid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy User")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with an invalid instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy User 12345")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test destroy command with a valid class and instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create User")
            obj_id = mock_stdout.getvalue().strip()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"destroy User {obj_id}")
            output = mock_stdout.getvalue().strip()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"show User {obj_id}")
            show_output = mock_stdout.getvalue().strip()

        self.assertIn("destroy User", output)
        self.assertEqual(show_output, "** no instance found **")


class TestHBNBCommandUpdate(unittest.TestCase):
    """Unittests for HBNBCommand update command."""

    def setUp(self):
        """Set up the test environment."""
        self.storage_file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove("test.json")
        except:
            pass
        FileStorage._FileStorage__file_path = self.storage_file_path

    def test_update_missing_class(self):
        """Test update command with missing class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with an invalid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update User")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with an invalid instance id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update User 12345")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_missing_attr_name(self):
        """Test update command with missing attribute name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update User 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing attribute value."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update User 123 name")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update(self):
        """Test update command with valid class, id, attribute name, and value."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create User")
            obj_id = mock_stdout.getvalue().strip()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"update User {obj_id} name John")
            output = mock_stdout.getvalue().strip()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"show User {obj_id}")
            show_output = mock_stdout.getvalue().strip()

        self.assertIn("update User", output)
        self.assertIn("name", show_output)


if __name__ == "__main__":
    unittest.main()

