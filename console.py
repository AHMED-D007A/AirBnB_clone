#!/usr/bin/python3
"""This is a module for CLI"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is CLI can be used to do operations(CRUD) on the site."""
    prompt = "(hbnb) "

    def emptyline(self):
        """handles empty inputs"""
        pass

    def do_EOF(self, arg):
        """This method is for end of the file."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
