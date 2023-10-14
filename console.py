#!/usr/bin/python3
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
    prompt = "(hbnb) "

    def do_quit(self, arg):

        return True
    def do_EOF(self, arg):
        return True
    def emptyline(self):
        return
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
