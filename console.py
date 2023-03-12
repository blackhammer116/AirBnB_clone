#!/usr/bin/python3
"""
Module that holds the command interpreter for the Airbnb Console
"""

import readline
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that extends cmd interpreter to allow the console to work
    """

    prompt = "(hbnb) "
    classes = [BaseModel.__name__, User.__name__, Amenity.__name__,
               City.__name__, Place.__name__, Review.__name__, State.__name__]

    def do_quit(self, arg):
        """
        Quits the interpreter loop
        """
        return True

    def help_quit(self):
        """
        Documentation for quit
        """
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        """
        command to handle EOF input
        """
        print()
        return True

    def help_EOF(self):
        """
        Documentation for EOF
        """
        print("EOF has been inputted so exit the program")
        print()

    def help_help(self):
        """
        Documentation for help command
        """
        print("Prints help information for commands")
        print()

    def emptyline(self):
        """
        Determines action when empty line is inputed
        """
        pass

    def parsecmd(self, commands):
        """
        Parse arguements to commands
        """
        li = []
        temp = commands.split('"')
        for i in range(len(temp)):
            if i % 2 == 0:
                li.extend(temp[i].split())
            else:
                li.append(temp[i])
        return li

    def do_create(self, args):
        """
        Creates and object of the specified instance type
        """

        cmds = self.parsecmd(args)
        if len(cmds) < 1:
            print("** class name missing **")
            return

        if cmds[0] == BaseModel.__name__:
            self.createObject(BaseModel)
        elif cmds[0] == User.__name__:
            self.createObject(User)
        elif cmds[0] == Amenity.__name__:
            self.createObject(Amenity)
        elif cmds[0] == City.__name__:
            self.createObject(City)
        elif cmds[0] == Place.__name__:
            self.createObject(Place)
        elif cmds[0] == Review.__name__:
            self.createObject(Review)
        elif cmds[0] == State.__name__:
            self.createObject(State)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
        Documentation for the create command
        """
        print("Create an object of specified type")
        print("create <class name>")
        print()

    def createObject(self, cls):
        """
        Create the object of class
        """
        obj = cls()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """
        show object with specified type and id
        """
        cmds = self.parsecmd(args)

        if len(cmds) < 1:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(cmds) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        obj = objects.get(f"{cmds[0]}.{cmds[1]}")
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def help_show(self):
        """
        Documentation for show command
        """
        print("Fetch object with specified class and id")
        print("show <class name> <id>")
        print()

    def do_destroy(self, args):
        """
        Destroy the object with specified class and id
        """
        cmds = self.parsecmd(args)

        if len(cmds) < 1:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(cmds) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        obj = objects.get(f"{cmds[0]}.{cmds[1]}")
        if obj:
            del objects[f"{cmds[0]}.{cmds[1]}"]
            obj.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """
        Documentation for destroy command
        """
        print("Delete object with specified class and id")
        print("destroy <class name> <id>")
        print()

    def do_all(self, args):
        """
        Fetch all object or objects of the specified type
        """
        cmds = self.parsecmd(args)
        objects = storage.all()
        obj_list = []
        if len(cmds) > 0:
            if cmds[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in objects.items():
                if value.__class__.__name__ == cmds[0]:
                    obj_list.append(str(value))
        else:
            for key, value in objects.items():
                obj_list.append(str(value))
        print(obj_list)

    def help_all(self, args):
        """
        Documentation for all command
        """
        print("Retrieve all objects or all objects of a specified type")
        print("all [<class name>]")
        print()

    def do_update(self, args):
        """
        Update command that updates the object with specified type and id
        """

        cmds = self.parsecmd(args)
        objects = storage.all()

        if len(cmds) < 1:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(cmds) < 2:
            print("** instance id missing **")
            return

        obj = objects.get(f"{cmds[0]}.{cmds[1]}")

        if obj is None:
            print("** no instance found **")
            return

        if len(cmds) < 3:
            print("** attribute name missing **")
            return
        if len(cmds) < 4:
            print("** value missing **")
            return

        key = cmds[2]
        val = type(getattr(obj, key, "Rand str"))(cmds[3])
        obj.__dict__[key] = val
        obj.save()

    def help_update(self):
        """
        Documentation for update command
        """
        print("Update the object specified with attribute and its value")
        print('update <class name> <id> <attribute name> "<attribute value>"')
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
