#!/usr/bin/python3
"""This is a module for CLI"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is CLI can be used to do operations(CRUD) on the site."""
    valid_classes = ["BaseModel", "User", "State", "Review",
                     "Place", "City", "Amenity"]
    prompt = "(hbnb) "

    def emptyline(self):
        """handles empty inputs\n"""
        pass

    def do_EOF(self, arg):
        """This method is for end of the file.\n"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
