from model import *
from controller import *
from cmd import Cmd

class MyPrompt(Cmd):

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit

    def do_start(self, args):
        """Starts the system."""
        system_1.start()

    def do_check(self, args):
        """Checks toner level in cartridge."""

        print(tube1.tonerLvl)

    def do_systeminfo(self, args):
        """Get tnformation about the system."""

        print(system_1.get_info())


    def do_addtnr(self, args):
        """Adds toner to the cartridge."""

        addToner()

    def do_print(self, args):
        """Prints some number of pages"""
        try:
            p = int(input("How many pages to print?: "))
            if (p*2) < tube1.tonerLvl:
                printing(p)
            else:
                print("Tube is empty..Add toner!")
        except ValueError:
            print()
            print("Write a number!")



if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Give the command...\nTo get list of commands and description write "help"')
