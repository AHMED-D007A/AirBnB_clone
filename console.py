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

    def do_User(self, args):
        """Usages: User.<method_name>()."""
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages: BaseModel.<method_name>()."""
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages: State.<method_name>()."""
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages: City.<method_name>()."""
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages: Amentiy.<method_name>()."""
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages: Place.<method_name>()."""
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages: Review.<method_name>()."""
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """Wrapper function for <class name>.action()"""
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
