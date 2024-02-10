#!/usr/bin/python3
"""This is the HBnB console."""
import cmd
from shlex import split
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if square_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:square_brackets.span()[0]])
            result_list = [i.strip(",") for i in lexer]
            result_list.append(square_brackets.group())
            return result_list
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        result_list = [i.strip(",") for i in lexer]
        result_list.append(curly_braces.group())
        return result_list

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (hbnb): My command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel"
    }

    def emptyline(self):
        """Ensures nothing is done upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            obj_id = args[1]
            key = f"{class_name}.{obj_id}"
            print(models.storage.all().get(key, "** no instance found **"))
        except IndexError:
            if class_name not in models.storage.all():
                print("** class doesn't exist **")
            elif len(args) == 0:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            obj_id = args[1]
            key = f"{class_name}.{obj_id}"
            instances = models.storage.all()
            if key in instances:
                instances.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if class_name not in models.storage.all():
                print("** class doesn't exist **")
            elif len(args) == 0:
                print("** instance id missing **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        instances = models.storage.all()
        if not arg:
            print([str(instance) for instance in instances.values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(instance) for key, instance in instances.items() if key.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            obj_id = args[1]
            key = f"{class_name}.{obj_id}"
            instances = models.storage.all()
            if key not in instances:
                print("** no instance found **")
                return

            instance = instances[key]
            attr_name = args[2]
            if len(args) == 3:
                print("** value missing **")
                return

            value = args[3]
            if hasattr(instance, attr_name):
                setattr(instance, attr_name, type(getattr(instance, attr_name))(value))
                models.storage.save()
            else:
                print("** attribute name missing **")

        except IndexError:
            if class_name not in models.storage.all():
                print("** class doesn't exist **")
            elif len(args) == 0:
                print("** instance id missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
