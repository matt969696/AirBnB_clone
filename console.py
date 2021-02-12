#!/usr/bin/python3
""" Module containing the console """

import shlex
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """My console"""
    prompt = '(hbnb)'
    classlist = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                 'Place', 'Review']

    def do_quit(self, arg):
        """Stops the console and quit"""
        return True

    def do_EOF(self, arg):
        """Stops the console and quit"""
        return True

    def emptyline(self):
        """Overwrite the emptyline method"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.classlist:
            newobj = eval(args[0] + '()')
            print(newobj.id)
            newobj.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.classlist:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        obj = args[0] + "." + args[1]
        if obj in models.storage.all():
            print(models.storage.all()[obj])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.classlist:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        obj = args[0] + "." + args[1]
        if obj in models.storage.all():
            models.storage.all().pop(obj)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = shlex.split(arg)
        printlist = []
        if len(args) == 0:
            for obj in models.storage.all().values():
                printlist.append(str(obj))
            print(printlist)
        elif args[0] in self.classlist:
            for key in models.storage.all().keys():
                if args[0] in key:
                    printlist.append(str(models.storage.all()[key]))
            print(printlist)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        intatt = ["number_rooms", "number_bathrooms", "max_guest",
                  "price_by_night"]
        floatatt = ["latitude, longitude"]
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.classlist:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        obj = args[0] + "." + args[1]
        if obj not in models.storage.all():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False
        inst = models.storage.all()[obj]
        if args[0] == "Place":
            if args[2] in intatt:
                try:
                    args[3] = int(args[3])
                except:
                    args[3] = 0
            if args[2] in floatatt:
                try:
                    args[3] = floatatt(args[3])
                except:
                    args[3] = 0
        setattr(inst, args[2], str(args[3]))
        inst.save()
        models.storage.reload()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
