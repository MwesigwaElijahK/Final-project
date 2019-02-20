class person:
    def __init__(self,person_name,role,housing):
        self.person_name = person_name
        self.role = role
        self.housing = housing

class staff(person):
    def __init__(self,person_name):
        self.person_name = person_name
        self.role = "staff"
        self.housing = False  

class fellow(person):
    def __init__(self,person_name):
        self.person_name = person_name
        self.role = "fellow"
        self.housing = True

    