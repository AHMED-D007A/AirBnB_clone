#!/usr/bin/python3
"""This is a module for CLI"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is CLI can be used to do operations(CRUD) on the site"""
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
        return True

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
        """Prints the representation of a instance based on the class name\n"""
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

    def do_count(self, arg):
        """count the number of existed instance."""
        args = arg.split()
        cownter = 0
        with open('file.json', 'r') as json_file:
            data = json.load(json_file)
        for key_id in data:
            key = key_id.split(".")
            if key[0] == args[0]:
                cownter += 1
        print(cownter)

    def do_User(self, arg):
        """Usages: User.<method_name>()."""
        self.class_exec('User', arg)

    def do_BaseModel(self, arg):
        """Usages: BaseModel.<method_name>()."""
        self.class_exec('BaseModel', arg)

    def do_State(self, arg):
        """Usages: State.<method_name>()."""
        self.class_exec('State', arg)

    def do_City(self, arg):
        """Usages: City.<method_name>()."""
        self.class_exec('City', arg)

    def do_Amenity(self, arg):
        """Usages: Amentiy.<method_name>()."""
        self.class_exec('Amenity', arg)

    def do_Place(self, arg):
        """Usages: Place.<method_name>()."""
        self.class_exec('Place', arg)

    def do_Review(self, arg):
        """Usages: Review.<method_name>()."""
        self.class_exec('Review', arg)

    def class_exec(self, cls_name, arg):
        """Wrapper function for <class name>.action()"""
        if arg[:6] == '.all()':
            self.do_all(cls_name)
        if arg[:8] == '.count()':
            self.do_count(cls_name)
        elif arg[:6] == '.show(':
            self.do_show(cls_name + ' ' + arg[7:-2])
        elif arg[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif arg[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + arg[10:-2])
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
