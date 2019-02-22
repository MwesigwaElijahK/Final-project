class rooms:
    def __init__(self,room_name,room_type,room_size):
        self.room_name = room_name
        self.room_type = room_type
        self.room_size = room_size
        self.occupants = []

class office(rooms):
    def __init__(self, room_name=None):
        self.room_name = room_name
        self.room_type = "office"
        self.room_size = 6 


class living_space(rooms):
    def __init__(self):
        self.room_name = room_name
        self.room_type = "living_space"
        self.room_size = 4         