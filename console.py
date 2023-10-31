#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
