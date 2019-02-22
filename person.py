class person:
    def __init__(self,person_name,role=None,accomodation = "N"):
        self.person_name = person_name
        self.role = role
        self.accomodation = accomodation

class staff(person):
    def __init__(self,person_name):
        self.person_name = person_name
        self.role = "staff"
        self.accomodation = "N"  

class fellow(person):
    def __init__(self,person_name):
        self.person_name = person_name
        self.role = "fellow"
        self.accomodation = True

    