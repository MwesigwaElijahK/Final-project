from Dojos import Dojo
from docopt import docopt, DocoptExit
import cmd
import sys


Usage = '''
    Office Space Allocation CLI

    Usage:
        Dojos.py init 
        Dojos.py create_room <room_name> <room_type>...
        Dojos.py person_added <person_name> <role> [accommodation]
'''

def docopt_cmd(func):
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            print("Invalid Command")
            print(e)  
            return
        except SystemExit: 
            return

        return func(self, opt)  

    fn.__name__ = func.__name__  
    fn.__doc__ = func.__doc__  
    fn.__dict__.update(func.__dict__) 
    return fn 

class Dojos(cmd.cmd):
    intro = "This is the Office Space Allocation CLI" \ 
        + " (type help for a list of commands) "   
    prompt = '(Dojos_CLI')
    file = None
    args = docopt(usage)
    office = []
    living_space = []

    def output_created_rooms(self,room_name,room_type)
        if type == 'office':
            appropriate_article = 'An'
            self.office.extend(room_name)
        else:
            appropriate_article = "A"
            self.living_space.extend(room_name)
        
        print("Office: ", self.office)
        print("living_space: ", self.living_space)

        for name in names:
            print("{} {} called {} has been successfully created!" .format(
                appropriate_article, room_type, room_name))


    @docopt_cmd
    def do_create_room(self, args):
        allowed_room_types = ["Office", "Living Space", "living"]          
        room_type = args["<room_type>"].lower()
        room_names = args['<room_name>']
        if room_type in allowed_room_types:
            self.output_created_rooms(room_name,room_type)
        else:
            print("{} is an invalid room type".format(room_type))

    def do_quit(self, arg):
        print("The CLI is being existed, GoodBye")
        exit()

Dojos().cmdloop()       