#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quits the console."""
        return True

    def help_quit(self):
        """Displays the help documentation for the 'quit' command."""
        print("Quit command to exit the program")

    def do_EOF(self, args):
        """Handles the EOF command."""
        return True

    def help_EOF(self):
        """Displays the help documentation for the 'EOF' command."""
        print("EOF command to exit the program")

    def emptyline(self):
        """Does nothing when receiving an empty line followed by ENTER."""
        pass

    def create(self):
        """Creates a new instance of BaseModel,
        saves it to JSON file and prints the id."""
        pass

    def show(self):
        """Prints the string representation of an instance
        based on the class name and id."""
        pass

    def destroy(self):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        pass

    def all(self):
        """Prints all string representation of all instances based
        or not on the class name."""
        pass

    def update(self):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
