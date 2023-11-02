#!/usr/bin/python3

import unittest
from unittest.mock import patch, create_autospec
from io import StringIO
from your_module import HBNBCommand, BaseModel, FileStorage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def assertCommandOutput(self, command_name, command_input, expected_output, mock_stdout):
        """Utility function to assert output of a command."""
        getattr(self.cli, f'do_{command_name}')(command_input)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_quit(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            self.cli.do_quit('')

    def test_EOF(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            self.cli.do_EOF('')

    # Continue with tests for each command
    # For example, testing 'create' command
    @patch('models.storage')
    def test_create(self, mock_storage):
        # Setup
        mock_storage.CLASS_DICT = {"BaseModel": BaseModel}
        
        # Test create without arguments
        self.assertCommandOutput('create', '', '** class name missing **')
        
        # Test create with non-existing class
        self.assertCommandOutput('create', 'MyModel', '** class doesn\'t exist **')
        
        # Test create with valid class
        mock_storage.CLASS_DICT["BaseModel"].return_value = BaseModel()
        self.assertCommandOutput('create', 'BaseModel', 'some-mocked-id')  # Adjust the expected output

        # Add more cases as needed

    # Similarly, add tests for do_show, do_destroy, do_all, do_update

if __name__ == "__main__":
    unittest.main()
