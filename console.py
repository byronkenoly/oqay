#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd


class OQAYCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = '(oqay) '

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