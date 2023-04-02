#!/usr/bin/env python3.10
"""
contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel


class OQAYCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = '(oqay) '
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
        elif arg2 == None:
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