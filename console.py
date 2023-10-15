#!/usr/bin/python3
"""the HBnB console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defining the command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        ]

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program.
        """
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        return True

    def do_create(self, line):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}")()
            print(new_instance.id)
            storage.save()

    def do_show(self, line):
        """Usage: show <class> <id>
        prints a string representation of an instance based on class name
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, line):
        """Usage: show <class> <id>
        Delets an instance based on the class name
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, line):
        """Usage: all or all <class>
        Display string representations of all instances of a class.
        If no class is given, displays all instantiated objects."""
        args = line.split()

        if len(args) == 0:
            print([str(val) for val in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            s = storage.all().items()
            print([str(val) for k, val in s if k.startswith(args[0])])

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing")
        else:
            objec_class = args[0]
            objec_id = args[1]
            objec_key = objec_class + "." + objec_id
            obj = storage.all()[objec_key]
            att_name = args[2]
            att_value = args[3]

            if att_value[0] == '"':
                att_value = att_value[1:-1]

            if hasattr(obj, att_name):
                type_ = type(getattr(obj, att_name))
                if type_ in [str, float, int]:
                    att_value = type_(att_value)
                    setattr(obj, att_name, att_value)
            else:
                setattr(obj, att_name, att_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
