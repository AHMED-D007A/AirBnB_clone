#!/usr/bin/python3
"""This is a module for CLI"""
import cmd
from models.base_model import BaseModel
from models import *


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
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        quit()

    def do_create(self, arg):
        """Creates a new instance of classes.\n"""
        args = arg.split()
        for argss in args:
            if argss not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
        if len(args) != 1:
            print("** class name missing **")
            return
        else:
            new_instance = eval(args[0])()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, arg):
        """Prints the representation of an instance based on the class name\n"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        switch = 0
        existed_instances = storage.all()
        for keys, values in existed_instances.items():
            key = keys.split(".")
            if key[1] == args[1]:
                switch = 1
                print(values)
                break
        if switch != 1:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id\n"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        switch = 0
        existed_instances = storage.all()
        for keys in existed_instances.keys():
            key = keys.split(".")
            if key[1] == args[1]:
                switch = 1
                del existed_instances[keys]
                storage.save()
                break
        if switch != 1:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name\n"""
        args = arg.split()
        for argss in args:
            if argss not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
        list = []
        existed_instances = storage.all()
        if len(args) != 0:
            for keys, values in existed_instances.items():
                key = keys.split(".")
                if key[0] == args[0]:
                    list.append(str(values))
        else:
            for value in existed_instances.values():
                list.append(str(value))
        print(list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)\n"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        switch = 0
        existed_instances = storage.all()
        for keys in existed_instances.keys():
            key = keys.split(".")
            if key[1] == args[1]:
                switch = 1
                setattr(existed_instances[keys], args[2], args[3][1:-1])
                storage.save()
                break
        if switch != 1:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
