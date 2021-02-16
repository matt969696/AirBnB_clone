#!/usr/bin/python3
""" Module containing the console """

import shlex
import cmd
import models
import re
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """My console"""
    prompt = '(hbnb) '
    classlist = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                 'Place', 'Review']
    funclist = ['all', 'count', 'show', 'destroy', 'update']

    def do_quit(self, arg):
        """Stops the console and quit"""
        return True

    def do_EOF(self, arg):
        """Stops the console and quit"""
        if sys.__stdout__.isatty():
            print("")
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

    def do_count(self, arg):
        """
        Counts all representation of all instances
        based or not on the class name
        """
        args = shlex.split(arg)
        countlist = 0
        if len(args) == 0:
            for obj in models.storage.all().values():
                countlist += 1
            print(countlist)
        elif args[0] in self.classlist:
            for key in models.storage.all().keys():
                if args[0] in key:
                    countlist += 1
            print(countlist)
        else:
            print("** class doesn't exist **")

    def update_parse(self, arg):
        listarg = []
        testdic = re.search(r"\{(.*?)\}", arg)
        if testdic is not None:
            parseddic = arg[testdic.span()[0]:testdic.span()[1]]
            parsed = shlex.split(arg[:testdic.span()[0]])
            for elem in parsed:
                listarg.append(elem)
            listarg.append(parseddic)
            parsed = shlex.split(arg[testdic.span()[1]:])
            for elem in parsed:
                listarg.append(elem)
        else:
            listarg = shlex.split(arg)
        return listarg

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        intatt = ["number_rooms", "number_bathrooms", "max_guest",
                  "price_by_night"]
        args = self.update_parse(arg)

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
            try:
                type(eval(str(args[2]))) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            inst = models.storage.all()[obj]
            if args[2] in inst.__class__.__dict__.keys():
                cast = type(inst.__class__.__dict__[args[2]])
                setattr(inst, args[2], cast(args[3]))
            else:
                setattr(inst, args[2], args[3])
        elif type(eval(str(args[2]))) == dict:
            inst = models.storage.all()[obj]
            for k, v in eval(args[2]).items():
                if k in inst.__class__.__dict__.keys():
                    cast = type(inst.__class__.__dict__[k])
                    setattr(inst, k, cast(v))
                else:
                    setattr(inst, k, v)
        inst.save()
        models.storage.reload()

    def precmd(self, line):
        """Method called before the line is interpreted"""
        parsed = ""
        test1 = line.find(".")
        if test1 == -1 or line[:test1] not in self.classlist:
            return line
        parsed1 = line[test1 + 1:]
        item1 = line[:test1]

        test2 = parsed1.find("(")
        if test2 == -1 or parsed1[:test2] not in self.funclist:
            return line
        parsed2 = parsed1[test2 + 1:-1]
        item2 = parsed1[:test2]

        parseddic = ""
        testdic = re.search(r"\{(.*?)\}", parsed2)
        if testdic is not None:
            parseddic = parsed2[testdic.span()[0]:]
            parsed2 = parsed2[:testdic.span()[0]]

        lexer = shlex.shlex(parsed2)
        lexer.whitespace += ','
        parsed3 = ""
        for token in lexer:
            parsed3 = parsed3 + " " + token

        finalline = item2 + " " + item1 + parsed3 + " " + parseddic
        return finalline

if __name__ == '__main__':
    HBNBCommand().cmdloop()
