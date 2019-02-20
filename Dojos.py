from rooms import *
from person import *

class Dojo:
    def __init__(self):
        self.totalRooms = []
        self.totalOffices = []
        self.living_spaces = []
        self.total_persons = []
        self.staff_persons = []
        self.fellow_persons = []
        self.unllocated_rooms = []
        self.allocated_rooms = []


def createRoom(self,room_name,room_type):
    if room_type == "office":
        newRoom = office(room_name)
        self.totalRooms.append(newRoom)
        self.totalOffices.append(newRoom)

    elif room_type == "livingSpace":
        newRoom = _space(room_name)
        self.totalRooms.append(newRoom)
        self.living_spaces.append(newRoom)

    else:
        return ("invalid room type. Only have office and livingSpace")

def personAdded(self,person_name,role,housing):
    if role == "staff":
        newPerson = staff(person_name)
        self.total_persons.append(newPerson)
        self.staff_persons.append(newPerson)

    elif role == "fellow":
        newPerson = fellow(person_name=person_name,housing=housing)
        self.total_persons.append(newPerson)
        self.fellow_persons.append(newPerson)
    else:
        return "There is no other role apart from staff and fellow"    

def assignRooms(self,person,housing):
