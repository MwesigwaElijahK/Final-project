from rooms import *
from person import *
import random

class Dojo:
    def __init__(self):
        self.total_rooms = []
        self.total_offices = []
        self.total_living_space = []
        self.total_persons = []
        self.staff_persons = []
        self.fellow_persons = []
        self.allocated = []
        self.unllocated = []
        self.unllocated_offices = []
        self.unllocated_living_space = []
        
    def create_room(self,room_name,room_type):
        if room_type == "office":
            new_room = office(room_name)
            self.total_rooms.append(new_room)
            self.total_offices.append(new_room)
            print("Office " + room_name  + " is created")

        elif room_type == "living_space":
            new_room = _space(room_name)
            self.total_rooms.append(new_room)
            self.living_spaces.append(new_room)
            print("living_space " + room_name  + " is created")

        else:
            return ("invalid room type. Only have office and livingSpace")

    def person_added(self,person_name,role,accomodation):
        if role == "staff":
            new_person = staff(person_name)
            self.total_persons.append(new_person)
            self.staff_persons.append(new_person)
            self.room_assign(new_person,accomodation=accomodation)

        elif role == "fellow":
            new_person = fellow(person_name=person_name,accomodation=accomodation)
            self.total_persons.append(new_person)
            self.fellow_persons.append(new_person)
            self.room_assign(new_person,accomodation=accomodation)

        else:
            return "There is no other role apart from staff and fellow"    

def room_assign(self,person,accomodation):
    
           