#!/usr/bin/env python3.10
"""
contains the entry point of the command interpreter
"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from datetime import datetime


class OQAYCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = '\033[1;35m(oqay)\033[0m '
    allowed_classes = ['BaseModel']

    def do_create(self, line):
        """
        Creates a new instance of BaseModel.
        saves it (to the JSON file) and prints the id
        """
        arg1 = self.parseline(line)[0]
        if arg1 == None:
            print("** class name missing **")
        elif arg1 not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            base_model_obj = BaseModel()
            base_model_obj.save()
            print(base_model_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        arg1 = self.parseline(line)[0]
        arg2 = self.parseline(line)[1]
        if arg1 == None:
            print("** class name missing **")
        elif arg1 not in self.allowed_classes:
            print("** class doesn't exist")
        elif arg2 == "":
            print("** instance id missing **")
        else:
            base_model_instance = models.storage.all().get(arg1 + '.' + arg2)
            if base_model_instance == None:
                print("** no instance found **")
            else:
                print(base_model_instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id 
        (save the change into the JSON file)
        """
        arg1 = self.parseline(line)[0]
        arg2 = self.parseline(line)[1]
        if arg1 == None:
            print("** class name missing **")
        elif arg1 not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg2 == None:
            print("** instance id missing **")
        else:
            key = arg1 + '.' + arg2
            base_model_instance = models.storage.all().get(key)
            if base_model_instance == None:
                print("** no instance found **")
            else:
                """
                ```del``` statement used to delete key 
                and value from dictionary
                """
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances 
        based or not on the class name
        """
        arg1 = self.parseline(line)[0]
        objs = models.storage.all()
        """
        objs is a dictionary that contains keys and values
        for obj in objs iterates over each key in the dictionary
        objs[obj] retrieves the value associated with current key
        """
        if arg1 == None:
            lst = []
            for key in objs:
                lst.append(str(objs[key]))
            print(lst)
        elif arg1 in self.allowed_classes:
            keys = objs.keys()
            lst = []
            for key in keys:
                if key.startswith(arg1):
                    lst.append(str(objs[key]))
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding 
        or updating attribute (save the change into the JSON file)
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print("** class name missing **")
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args[1] == None:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data == None:
                print("** no instance found **")
            elif args_size == 2:
                print("** attribute name missing **")
            elif args_size == 3:
                print("** value missing **")
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()

    def analyze_parameter_value(self, value):
        """Checks a parameter value for an update
        Analyze if a parameter is a string that needs
        convert to a float number or an integer number.
        Args:
            value: The value to analyze
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value

    def do_quit(self, line):
        """
        exits the program
        """
        return True

    def do_EOF(self, line):
        """
        exits the program
        """
        return True

    def emptyline(self):
        """
        an empty line + ENTER shouldn't execute anything
        """
        pass


"""
This portion runs only when file is executed as a script
"""
if __name__ == '__main__':
    OQAYCommand().cmdloop()