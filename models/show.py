class Show(object):
    def __init__(self, id : int, name : str, date : str, capacity : bool, description : str, room : list) -> None:
        self.id = id
        self.show_name = name
        self.date = date
        self.capacity = capacity
        self.description = description
        self.room = room
    
    def GetID(self):
        return self.id

    def GetShowName(self):
        return self.show_name

    def GetDate(self):
        return self.date

    def GetCapacity(self):
        return self.capacity

    def GetDescription(self):
        return self.description

    def GetRoom(self):
        return self.room

    def getSeatNumber(self,room_index : tuple):
        pass